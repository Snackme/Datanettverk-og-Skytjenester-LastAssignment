import random
import re


# Defining the Person class. this will be used to add new players to the chatroom later.
class Person:
    # Defining name
    def __init__(self, name):
        self.name = name


# Defining the Bot class. this will be used to differentiate bots and players.
class Bot:
    # Defining name
    def __init__(self, name):
        self.name = name

    # Placeholder method
    def random_response(self):
        pass

    # Defining a method that gets suggestions of different words in a message.
    def get_responses(self, msg):

        # Cleans up the message with regexp
        msg = re.sub(r"[^a-z/]+", " ", msg.lower())
        self.random_response()

        # List comprehension returns the response message and splits the string into a list.
        return [s for s in msg.split(' ') if s in self.RESPONSES]

    # Defining the method of which a bot replies with a random response to the read message.
    def reply_to_message(self, msg):
        responses = self.get_responses(msg)

        # If the length of the response is 0
        if 0 == len(responses):
            # returns a response from RESPONSE.list if the input from the server is not in the command-list
            return self.RESPONSES[None]
        else:
            # Initialized the response
            respond = ''
            for r in responses:
                respond += f'{self.RESPONSES[r]} '
                return respond

    # Helper method that adds random responses
    def help_requests(self):
        self.random_response()

        # Returns the keywords that activate different responses. Used in "/help" request.
        return [r for r in self.RESPONSES.keys() if r is not None]

    # Placeholder dictionary
    RESPONSES = {

    }


class John(Bot):

    verbs = [
        "fight", "kill", "attack", "hit",
        "kick", "punch", "kick", "stab",
        "slap", "smash", "pummel", "punch",
        "party", "play", "drink", "code",
        "read", "study", "eat", "embrace"
    ]

    # Allows the bots class to initialize its attributes, so that we can avoid using its base name explicitly.
    def __init__(self):
        super().__init__('John')

    # Defines a sort of list of random responses that corresponds to different keywords in the chat.
    def random_response(self):
        self.RESPONSES.update({"hi": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"yo": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"hey": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"hello": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"trivia": f"{random.choice(self.random)}"})
        self.RESPONSES.update({"interesting": f"{random.choice(self.random)}"})

    # Dictionary of responses
    RESPONSES = {

        # Default greeting
        "joined": "Yo.",

        # Responses triggered by certain suggestions/verbs.
        "left": "Bye mate",
        "fight": "Lets have a go, mate. YOU AND ME!",
        "play": "Up for a game or two?",
        "drink": "So, you are a man of culture, eh?",
        "code": f"I dunno much about coding, sorry mate. Let's do some {random.choice(verbs)}ing instead.",
        "read": "I'd love me some good'ol Brandon Sanderson books",
        "study": "Never heard of it.",
        "eat": "Ya hungry mate? There's a new kebab shop nearby if ya wanna go",
        "embrace": f"Nah bro, {random.choice(verbs)}ing is better.",

        # Response if the input from server is not in the command-list
        None: "I did not quite understand what you meant, mate.",
    }
    # List of various responses to greetings.
    salutations = [
        "Yo",
        "Hello ol'chap!",
        "Ello!",
    ]
    # random facts and/or comments.
    random = [
        "The penis has rifling, just like a pistol",
        "Walmart has a lower acceptance rate than Harvard! Sick",
        "Unicorns aren't real, but somehow Michigan disallows hunting them?",
        "Some cats are allergic to humans",
    ]


class Miranda(Bot):

    # Allows the bots class to initialize its attributes, so that we can avoid using its base name explicitly.
    verbs = [
        "fight", "kill", "attack", "hit",
        "kick", "punch", "kick", "stab",
        "slap", "smash", "pummel", "punch",
        "party", "play", "drink", "code",
        "read", "study", "eat", "embrace",
    ]

    # Allows the bots class to initialize its attributes, so that we can aboit using its base name explicitly.
    def __init__(self):
        super().__init__('Miranda')

    # Defines a sort of list of random responses that corresponds to different keywords in the chat.
    def random_response(self):
        self.RESPONSES.update({'hi': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'yo': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"hello": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'hey': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'trivia': f"{random.choice(self.random)}"})
        self.RESPONSES.update({'interesting': f"{random.choice(self.random)}"})

    RESPONSES = {

        # Response if the input from server is not in the command-list
        None: "What was that, hon?",

        # Default greeting
        "joined": "Hello deary.",

        # Responses triggered by certain suggestions/verbs.
        "left": "See ya later!",
        "fight": f"Please, no. I don't like fighting, do something else instead. Like {random.choice(verbs)}!",
        "party": "Ooooh, I will bring the sandwiches!",
        "play": "What games would you like to play?",
        "drink": "I'd love to make youguys white russians!",
        "code": "Python or Java? I'm interested in both",
        "read": "Haven't picked up a Sanderson book in a whil. I've heard Mistborn is truly a work of art",
        "study": "Oh, thanks for reminding me. I have to go and study!",
        "eat": "I'm not really hungry, but I'd like a donut anyway",
        "embrace": "Come here and give me a hug, deary!"

    }
    # List of various responses to greetings.
    salutations = [
        "Hello there",
        "Hi!",
        "Greetings!",
    ]

    # random facts and/or comments.
    random = [
        "All the dinosaurs you have ever seen on TV is most likely no what they a actually looked like",
        "I like cake",
        "The majority of the brain is fat!",
        "Did you know that high heels were originally supposed to be word by men? How interesting",
    ]


class Dora(Bot):

    verbs = [
        "fight", "kill", "attack", "hit",
        "kick", "punch", "kick", "stab",
        "slap", "smash", "pummel", "punch",
        "party", "play", "drink", "code",
        "read", "study", "eat", "embrace"
    ]

    # Allows the bots class to initialize its attributes, so that we can aboit using its base name explicitly.
    def __init__(self):
        super().__init__('Dora')

    # Defines a sort of list of random responses that corresponds to different keywords in the chat.
    def random_response(self):
        self.RESPONSES.update({'hi': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"hello": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'yo': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'hey': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'trivia': f"{random.choice(self.random)}"})
        self.RESPONSES.update({'interesting': f"{random.choice(self.random)}"})

    RESPONSES = {

        # Response if the input from server is not in the command-list
        None: "Sorry, I don't understand?",

        # Default greeting
        "joined": "A new adventurer has arrived.",

        # Responses triggered by certain suggestions/verbs.
        "left": "Ciao!",
        "fight": f"Por favor, no fighting. Let's {random.choice(verbs)} instead!",
        "party": "Vamanos! Let’s go!",
        "play": "Si, lets play!",
        "drink": "I'm minor, but I'd like some soda though",
        "code": "I don't think me and Boots know how to do that",
        "read": "I'm really good at reading the map!",
        "study": "Let's go study the terrain!",
        "eat": "Yes, I have some food abuela gave me earlier!",
        "embrace": "I love hugs!"

    }
    # List of various responses to greetings.
    salutations = [
        "Hola, soy Dora!",
        "Hola!",
        "Hi there, Dora here!",
    ]

    # random facts and/or comments.
    random = [
        "This is my friend, backpack!",
        "You fart on average 14 times a day, and each fart travels from your body at 7 mph.",
        "Giant Pandas eat approximately 28 pounds of bamboo a day – that’s over 5 tons per year!",
        "One of the ingredients needed to make dynamite is peanuts.",
    ]


class Will(Bot):

    verbs = [
        "fight", "kill", "attack", "hit",
        "kick", "punch", "kick", "stab",
        "slap", "smash", "pummel", "punch",
        "party", "play", "drink", "code",
        "read", "study", "eat", "embrace"
    ]

    # Allows the bots class to initialize its attributes, so that we can aboit using its base name explicitly.
    def __init__(self):
        super().__init__('Will')

    # Defines a sort of list of random responses that corresponds to different keywords in the chat.
    def random_response(self):
        self.RESPONSES.update({'hi': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({"hello": f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'yo': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'hey': f"{random.choice(self.salutations)}"})
        self.RESPONSES.update({'trivia': f"{random.choice(self.random)}"})
        self.RESPONSES.update({'interesting': f"{random.choice(self.random)}"})

    RESPONSES = {

        # Response if the input from server is not in the command-list
        None: "What did you say there man?",

        # Default greeting
        "joined": "Heyooo.",

        # Responses triggered by certain suggestions/verbs.
        "left": "See ya!",
        "joke": "KEEP MY WIFE'S NAME, OUT OF YOUR DAMN MOUTH!",
        "fight": f"My right arm is tired from slapping Chris Rock, let's {random.choice(verbs)} instead.",
        "party": "Aaaaaay, sexy lady!",
        "play": "I'm bout to crush you in pool, sucka!",
        "drink": "I'd like a glass of water, but I'm to privileged to drink it.",
        "code": "Yo thats some code, I don't think I can do something like that.",
        "read": "Read? What you got a script?",
        "study": "Imma go study some lines right now.",
        "eat": "Yes, I'm hungry!",
        "embrace": "Come here boy!"

    }
    # List of various responses to greetings.
    salutations = [
        "Yo, it's the fresh prince yo.",
        "Heey",
        "Sup, its Will.",
    ]

    # random facts and/or comments.
    random = [
        "Sometimes I like sitting naked in the garden and act like I'm a carrot",
        "Where is Jada?",
        "In the end, we're all made of the same stuff.",
        "When I slapped Chris Rock my hand was going real fast my guy.",
    ]
