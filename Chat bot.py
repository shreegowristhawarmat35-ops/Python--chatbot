print("Hello! I am a simple chatbot. Type 'exit' to stop.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi there!")
    elif user_input == "how are you":
        print("Bot: I'm just code, but I'm doing great!")
    elif user_input == "your name":
        print("Bot: I am a Python chatbot.")
    elif user_input == "exit":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
