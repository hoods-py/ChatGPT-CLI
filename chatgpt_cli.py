#!/usr/bin/env python3
import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
# Load dotenv
load_dotenv()

# Get key
openai_key = os.environ.get('OPENAI_API_KEY')

# Initialize client
client = OpenAI(
    api_key=openai_key
)

def chat(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])

    # Get the model's response
    response_content = response['choices'][0]['message']['content']

    return response_content

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        print(chat(prompt))
    else:
        print("Usage: chatgpt.py [PROMPT]")


