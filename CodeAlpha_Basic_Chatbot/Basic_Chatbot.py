def chatbot():
    print("Hello! I'm your simple chatbot.")
    print("Type 'bye'to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hi there! Nice to talk to you.")

        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking! How about you?")

        elif "i'm doing well too" in user_input:
            print("Bot: That's great to hear! How can I assist you today?")

        elif "what's up" in user_input:
            print("Bot: Not much, just chatting with you!")

        elif "your name" in user_input:
            print("Bot: I'm a simple rule-based chatbot created in Python.")

        elif "help" in user_input:
            print("Bot: I can respond to greetings, ask about your day, and have simple conversations. Try saying 'hi' or asking 'how are you?'")

        elif "thank" in user_input:
            print("Bot: You're welcome! Happy to help.")

        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Hmm... I don't understand that yet, but I'm learning!")

chatbot()
