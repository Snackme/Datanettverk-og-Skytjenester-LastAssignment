import socket
import threading
import dill
import sys
import Party
import re


# Helps and forces user to connect with ip and port.
try:

    # This is the list of bots
    bot_list = {
        "john": Party.John(),
        "miranda": Party.Miranda(),
        "dora": Party.Dora(),
        "will": Party.Will(),
    }

# Declares IP as command line argument 1
    IP = sys.argv[1]

    # If the user asks for help, print out helping messages.
    if IP == "-h" or IP == "--help":

        # Very detailed message (hehe)
        print("\nTo connect to the client, please use example command: \n$ python client.py 'IP' 'Port'\n"
              f"(An example would be: python client.py 'IP' 'Port') \n")
        print("Want to connect a bot? Pick from this list: \n"
              f"{list(bot_list.keys())}\n"
              f"(An example would be: python client.py 'IP' 'Port' 'botName')")
        sys.exit()

    # Declares PORT as command line argument 2
    PORT = int(sys.argv[2])
    if PORT == "-h" or PORT == "--help":

        # Very detailed message (hehe)
        print("\nTo connect to the client, please use example command: \n$ python client.py 'IP' 'Port'\n")
        print("Want to connect a bot? Pick from this list: \n"
              f"{list(bot_list.keys())}\n"
              f"An example would be: python client.py 'IP' 'Port' 'botName'")
        sys.exit()


# Recognizes typo, and explained this to the user.
except (ValueError, IndexError):
    print("Please specify IP and PORT. Example would be: $python client.py localhost 1111")
    sys.exit()


# Making sure client connections can choose name and/or choose bots
try:
    # If there is not a 4th command line argument, then it must be a connecting user
    if len(sys.argv) != 4:
        # Let the user pick a nickname
        user = Party.Person(input('Please enter a nickname: '))
    else:
        # Else, the connection is trying to connect a bot.
        # Takes the bot dictionary and matches it with the input, and makes it a 3rd line argument
        user = bot_list[sys.argv[3].lower()]

# Recognize a typo, and write out a list of available bots.
except KeyError:
    print(f'Sorry, {sys.argv[3]} is not available. Here is a list of the bots that you can use: \n'
          f'{list(bot_list.keys())}')
    sys.exit()

# Creating the TCP connection
client = socket.socket()
try:
    # Try to connect the client to the IP and PORT
    client.connect((IP, PORT))

# Exception when the ip and port cannot be connected to
except ConnectionRefusedError:

    # Prints out exactly what ip and port that cannot be reached.
    print(f'This IP: {IP} and PORT: {PORT}, cannot be reached.')
    sys.exit()

# Sends a message to server about new connection.
client.send(dill.dumps(user))


# Method to receive broadcast messages.
def get_messages():

    # While we're able to get messages:
    while True:
        # Try function
        try:
            # This tells the server to send back the user and the message that the user wrote.
            # Using dill to serialize the send, and get_msg objects
            send, get_msg = dill.loads(client.recv(1024))

            # This prints the sent message.
            if "server" == send.name:
                print(f'{get_msg}')
            else:
                if user.name != send.name:
                    print(f'{send.name}: {get_msg}')

            # This checks if the sent message comes from a person, or a bot:
            if isinstance(user, Party.Bot) and isinstance(send, Party.Person):
                # If the connected client is a bot, but the sender is a person
                # then this lets the bot reply to the message.
                bot_resp = user.reply_to_message(get_msg)
                # Prints out the bots response
                print(f'{user.name}: {bot_resp}')
                # Collects and stores the bots response
                inputs = dill.dumps((user, bot_resp))
                # Sends the bots response to all other clients.
                client.send(inputs)

        # The error-message will appear after a slight delay, to see if the errors fix themselves first.
        except (OSError, ConnectionResetError, EOFError):

            # Prints errormessage cause of unknown errors, or kick.
            print('You have been disconnected')

            # Closes client and breaks from the connection.
            client.close()
            break


# Now, to start the threads and run the functions at the same time:
receive_thread = threading.Thread(target=get_messages)
receive_thread.start()


# function that makes user able to send messages.
# only persons and host can send messages.
def send_messages():

    # While we're able to send messages.
    while True:

        # Try function
        try:
            # Checking if the client is connected to the server with empty string.
            client.send(dill.dumps((user, '')))

            # This cleans up the messages.
            send_msg = re.sub('[ ]+', ' ', input().strip())

            # If-function that performs the /logout command, and nothing else.
            if send_msg == '/logout':
                client.close()
                break

            # Runs the function with the cleaned up message.
            do_request(send_msg)

            # Stores and sends the message to all other clients and server.
            client.send(dill.dumps((user, send_msg)))

        # Unknown errormessage that happens when user is somehow unable to connect to the server.
        except (EOFError, ConnectionAbortedError, OSError):
            print('Problem with connecting to the server, sorry :/')

            # Closes client and breaks the connection
            client.close()
            break


# Only start if the person is the one sending the messages.
if isinstance(user, Party.Person):
    write_thread = threading.Thread(target=send_messages)
    write_thread.start()


# Defining request function
def do_request(req_msg):

    # Splits the request string into a list.
    request = req_msg.split(' ')
    if request[0] in requests:

        # Rejoins the message, but excludes command
        requests[request[0]](' '.join(map(str, request[1:])))


# Defining the client-side of changing a name
def new_name(new):

    # Initiates the old username value
    old = user.name

    # Initializes new username
    user.name = new

    # returns empty string.
    return old


# Puts new_name in a dict. so that it also works on the server.
requests = {
    '/new_name': new_name,
}

sys.exit()
