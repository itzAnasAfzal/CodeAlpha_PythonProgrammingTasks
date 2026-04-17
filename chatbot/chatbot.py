
class ChatBot:
    def __init__(self):
        # Predefined responses (rules)
        self.responses = {
            "hello": "Hi!",
            "hi": "Hello!",
            "how are you": "I'm fine, thanks!",
            "bye": "Goodbye!",
            "what is your name": "I am a simple chatbot.",
            "help": "You can say hello, ask how I am, or say bye."
        }

    def get_response(self, user_input):
        # Convert input to lowercase for matching
        user_input = user_input.lower()

        # Check predefined responses
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "Sorry, I don't understand that."

    def run(self):
        print("ChatBot is running... (type 'bye' to exit)\n")
        
        runing = True
        while runing:
            user_input = input("You: ")

            response = self.get_response(user_input)
            print("Bot:", response)

            if user_input.lower() == "bye":
                runing = False


# Create object and start chatbot
bot = ChatBot()
bot.run()


input("ChatBot terminated. Thank you!\nPress Enter to exit...")