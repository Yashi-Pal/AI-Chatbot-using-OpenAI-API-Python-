def chatbot():
    print("🤖 AI Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?\n")

        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm doing great 😄\n")

        elif "what is ai" in user_input:
            print("Chatbot: AI (Artificial Intelligence) is the simulation of human intelligence by machines.\n")

        elif "python" in user_input:
            print("Chatbot: Python is a powerful programming language used in AI, data science, and web development.\n")

        elif "bye" in user_input:
            print("Chatbot: Bye! Have a great day 👋\n")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that. Try asking something else.\n")


if __name__ == "__main__":
    chatbot()