import openai

openai.api_key = "OPENAI API KEY"

engine = "text-davinci-002"

def start_chat():
    print("Hello! What do you want to ask Chat GPT?")
    while True:
        user_input = input("Prompt: ")
        if user_input.lower() == "end":
            break
        response = openai.Completion.create(
            engine=engine,
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text
        print("Chat GPT:", message)

start_chat()
