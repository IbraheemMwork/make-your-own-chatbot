from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(
    api_key=" put ur API key here"
)

# Function to chat with GPT
def chat(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Run chatbot loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        reply = chat(user_input)
        print("Chatbot:", reply)