from openai import OpenAI
import os

#please change reference KEY go to https://platform.openai.com/api-keys
client = OpenAI(api_key=" put ur API key here")

#function to create chat with GPT
def chat(prompt):
    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

#exiting chatbot
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response = chat(user_input)
        print("chatbot: ", response)