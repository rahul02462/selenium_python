def get_bot_response(user_input):
    if user_input.lower() == 'hey':
        return "Hello welcome to chatbot"
    elif user_input.lower() == 'how are you':
        return "I am fine! how are you??"
    else:
        return "Thank you for using chatbot"

while True:
    x = input("You: ")
    if x.lower() == 'bye':
        break
    get_response = get_bot_response(x)
    print("ChatBot",get_response)