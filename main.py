import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Create the OpenAI client
client = openai.OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        try:
            response = chat_with_gpt(user_input)
            print("Chatbot:", response)
        except Exception as e:
            print("Error:", e)
