import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello', ['Hello!', 'Hi there!']),
    (r'how are you?', ['I am fine, thank you!', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by Python.']),
    (r'quit', ['Goodbye!', 'Have a nice day!']),
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

if __name__ == "__main__":
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() == 'quit':
            break
