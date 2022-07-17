#DATA2410. Portfolio Assignment1: Socket Bots

*This is the first individual portfolio assignment in DATA2410. The task was to create a simple chatbot* 
*<br /> that we would be able to interact with through a TCP connection.*

## Before running
You should install dill, if you haven't already. Just type in e.g *pip install dill* in the command line in powershell or whatever program you're using.

## How to run the program:
1. Start by navigating to the directory the file is in your terminal window, then type in e.g: python server.py localhost 1111

    - The server will then give you a message, saying it has connected successfully and gone into listening mode. 
2. Open up another terminal and navigate to the same file, except you'll have to type this in instead: python client.py localhost 1111

    - The client will then ask you to present it with a nickname, you can choose which one you want. 
    - If you'd rather connect a bot, then you could type in the name of one of the available bots after the PORT key. 
    <br/> Like this: python client.py localhost 1111 John
3. You can open up as many terminals as you want and connect them to the server, but I'd recommend 2 bots and 1 "user" client for convenience's sake. 
4. Now you can interact with the bots. Although the keywords to make the bots respond in different ways are somewhat limited, you could try one of these basic keywords like: 'walk', 'dance', 'fight'
    
    - You will notice that the bots will have different reactions to each keyword. 
5. There are also requests you can make from the server. To view available requests, just type in "/help" in the command line window of your user connection-
6. To disconnect, just close the terminal windows. You can also write in /close to sever all connections.
