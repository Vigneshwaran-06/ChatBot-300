
import random  
import nltk  
from nltk.chat.util import Chat, reflections  
from transformers import pipeline  

# Load a Hugging Face conversational model  
chatbot_pipeline = pipeline("conversational", model="facebook/blenderbot-400M-distill")  

responses = [  
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello!", "Hey there!", "Hi! How can I assist you today?"]],  
    [r"(.*) your name ?", ["I'm Ninja, an AI chatbot built to assist you!",]],  
    [r"(.*) help (.*)", ["I'm here to help! What do you need assistance with?",]],  
    [r"how are you (.*) ?", ["I'm an AI, but I'm always ready to assist!", "I'm functioning optimally!",]],  
    [r"sorry (.*)", ["No worries! How can I assist you?",]],  
    [r"quit", ["Goodbye! Have a great day!", "See you soon!", "It was nice talking to you!"]],  
    [r"(.*)", ["That’s interesting!", "Tell me more!", "I'm listening!", "Would you like to ask something else?"]],  
]  

class AdvancedChatbot(Chat):  
    def __init__(self, pairs, reflections):  
        super().__init__(pairs, reflections)  
    
    def converse(self):  
        print("Hi, I'm Ninja AI! How can I help you? (Type 'quit' to exit)")  
        while True:  
            user_input = input("You: ")  
            if user_input.lower() == "quit":  
                print(random.choice(["Goodbye! Have a great day!", "See you soon!"]))  
                break  
            # Use Hugging Face model for improved conversation  
            response = chatbot_pipeline(user_input)  
            bot_reply = response[0]['generated_text'] if response else super().respond(user_input)  
            print(f"Ninja: {bot_reply}")  

# Initialize and start chatbot  
chatbot = AdvancedChatbot(responses, reflections)  
chatbot.converse()  
