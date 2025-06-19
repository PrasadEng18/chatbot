def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there!")
        
        elif user_input in ["how are you", "how's it going"]:
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input in ["what's your name", "who are you"]:
            print("Chatbot: I'm a simple chatbot.")
        
        else:
            print("Chatbot: Sorry, I don't understand.")

if __name__ == "__main__":
    chatbot()