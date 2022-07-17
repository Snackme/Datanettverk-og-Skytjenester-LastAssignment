import socket
import threading
import sys
import dill
import Party

# Defining a try method of forcing the user to choose and IP or PORT,
# with examples if an error should occur
try:
    # Declares IP as command line argument 1
    IP = sys.argv[1]
    if IP == "-h" or IP == "--help":
        print("To start the server, please use example command: python server.py 'IP' 'PORT' ")

        # sys.exit() Terminates connection if args. has not been passed to the commandline
        sys.exit()

    # Declares PORT as command line argument 2
    PORT = int(sys.argv[2])
except (ValueError, IndexError):
    print("Please specify IP and PORT. \n"
          "Example would be: $python server.py localhost 1111")

    # sys.exit() Terminates connection if args. has not been passed to the commandline
    sys.exit()

# Creating socket connection, binding IP and PORT and making the server listen.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding IP and PORT to server
server.bind((IP, PORT))

# Tells server to continually listen
server.listen()

# Defines server connection as "host" with a username.
HOST = Party.Person("Host")

# Defining a clients list to put all the connected clients in.
client_dict = {}

# Prints out confirmation of successful server connection
print("Server is now up and running!")
print("Server is listening for new connections ... ")


# Defining function to broadcast all the messages to all clients.
def broadcast_data(sent, msg):
    for connected in client_dict:

        # Using dill.dump to serialize and store arguments and data sent.
        data = dill.dumps((sent, msg))

        # Sends the collected data to all other clients.
        connected.send(data)


# Defining a handle function to organize and send all messages from all clients.
def handle(h):
    while True:
        try:
            # We say as long as we receive messages from the client,
            # we are going to broadcast the messages to all other clients.
            # Including this one.
            sent, msg = dill.loads(h.recv(1024))
            if len(msg) > 0 and not do_request(h, msg):

                # Prints the username and message
                print(f"{sent.name}: {msg}")

                # broadcasts the username and message
                broadcast_data(sent, msg)

        # Exception if someone leaves the server or the chat
        except ConnectionResetError:

            # Removes the dicsonnecting client from the list.
            index = client_dict.pop(h, Party.Bot("Someone"))

            # Prints the message of the disconnected clients
            print(f'{index.name} just disconnected from the server!')

            # Broadcasts the message of the disconnected clients.
            broadcast_data(Party.Person("server"), f"{user.name} has left the chat!")
            h.close()
            break

        # Exception to stop server from disconnecting.
        except ConnectionAbortedError:
            break


# Makes it so that host also can write messages.
def host_write():
    while True:
        i = input('')

        # If the hosts message is not a request, and the messages length is bigger than 0,
        # then it hosts message is broadcast
        if do_request(HOST, i) or len(i) <= 0:
            continue

        # broadcasts the hosts messages
        broadcast_data(HOST, i)


# Hosts thread.
thread_host = threading.Thread(target=host_write)
thread_host.start()


# Defines a function that makes sure changes by the client is mirrored in the server,
# to make sure that the correct objects are handled.
def do_request(doReq, msg):

    # To do this, we turn the message into an array
    r = msg.split(" ")
    if r[0] in requests:

        # Rejoins the message, but excludes command
        argument = ' '.join(map(str, r[1:]))

        # joins the command, client and the argument parameters together.
        requests[r[0]](doReq, argument)

        # returns true for found requests.
        return True
    # returns false if no requests were found
    return False


# Defines a function that lets users and client ask for the requests-lSist that they can make from the server.
def help_requests(help, emptyArg):

    # lists the request-dictionary.
    request_list = list(requests.keys())

    display_help = f'These are the requests you can make: \n' \
                   f'{request_list}'
    for c in client_dict:

        # If a bot is connected, the /help request will add a list of requests that the bots will respond to.
        if isinstance(client_dict[c], Party.Bot):
            display_help += f'\nThese are the requests the bot: ' \
                            f'{client_dict[c].name} will respond to' \
                            f' \n{client_dict[c].help_requests()}'

    # If its the host thats asking for requests
    if help == HOST:

        # Prints the help string
        print(display_help)
    else:

        # Stores and serialized the connected bots, and their display_help list.
        data = dill.dumps((Party.Bot('server'), display_help))
        # Send the stored data.
        help.send(data)


# Defines function to let users change their name
def new_name(user, new):

    # Makes sure that host cannot change name:
    # If serverhost tries to change name, then an error message will appear:
    if user == HOST:
        print("Host cannot change name")
    else:
        # Broadcasts all requests to the other clients, if its being performed
        # will be broadcasted as a bot, as we dont want the bots to respond to the requests.
        broadcast_data(Party.Bot('server'), f'{client_dict[user].name}s name has been changed to: {new}')

        # Clients will then get the updated name
        client_dict[user].name = new


# Defining close function which disconnects the server. Needs an empty argument to not get TypeError
def close(close, emptyArg):

    # If a connected client is closing the server.
    if close in client_dict:

        # Prints for the server who is disconnecting
        print(f'{client_dict[close].name} is disconnecting.')

        # Broadcasts for everyone who is disconnecting
        broadcast_data(Party.Bot('server'), f'{client_dict[close].name} is disconnecting.')
    else:
        # Else we say that the server(host) itself is closing the server
        broadcast_data(Party.Bot('server'), f'The host is closing down the server!')

    # Takes down every connection.
    for cl in client_dict:
        cl.close()
    # Clears the client
    client_dict.clear()

    # Closes server
    server.close()

    # Exits system
    sys.exit()


# Defining simple kick function.
def kick(emptyArg, user):

    # This is the standard for those who is kicked, also none has been kicked yet.
    kicked = None
    for c in client_dict:

        # Basically says that if the name written in the client is the same as the name of a connected user,
        # then it will broadcast a "kicked" message.
        if user.lower() == client_dict[c].name.lower():
            kicked = c

            # Broadcasts who got kicked from the chat as a bot, since we don't want bots to respond to the message.
            broadcast_data(Party.Bot('server'), f'{client_dict[c].name} got kicked from the chat!')
            print(f'{client_dict[c].name} got kicked from the server!')

    # if the kicked user is connected, then the user will be disconnected.
    if isinstance(kicked, socket.socket):

        # Removes kicked client connection from the list.
        client_dict.pop(kicked)

        # Closes kicked client.
        kicked.close()


# Dictionary of requests a user can make from the server.
requests = {
    '/help': help_requests,
    '/new_name': new_name,
    '/close': close,
    '/kick': kick
}

# This is our main "function" for making the server run. The whole thing says basically that as long as
# the server is running, tell the server to accept all connections, then an object receives the connected clients data.
# As long as the server is running
while True:
    try:
        # Tells the server to accept every connection
        client, (IP, PORT) = server.accept()
    except OSError:
        print(f'Disconnected at IP:{IP} and PORT: {PORT}')
        break

    # this receives the connected clients data
    user = dill.loads(client.recv(1024))

    # Printing the info for system.
    print(f'\nSensing new connection on IP:{IP} and PORT: {PORT} \n'
          f'{user.name} has successfully joined the server!')

    # Now we make a sort of list of connected clients whenever a new one connects.
    # This is done using dictionary since it accesses the items faster.
    client_dict.update({client: user})  # Updates the value pairs and overwrites existing keys
    cl_thread = threading.Thread(target=handle, args=(client,))
    cl_thread.start()

    # broadasts new connection to everyone
    broadcast_data(Party.Person('server'), f'Drumroll please .... \n'
                                           f'{user.name} has joined the chat!')

