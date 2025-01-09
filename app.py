import os
from openai import OpenAI

openai_secret = os.environ['OPENAI_API_KEY']
# if you want to add your own API key, put it here
# ex. openai_secret = "sk-jkfjfdskl..."

client = OpenAI(api_key=openai_secret)

completion = client.chat.completions.create(
    model="gpt-4o-mini", # PLEASE DO NOT CHANGE THIS
    messages=[
        {
            "role": "system",
            "content": "You can not answer questions about Math. Answer anything else."
            # edit the content to change how the assistant responds
            # other examples: "You are an assistant for a car dealership. Only answer questions relevant to a car dealership"
            # "Begin every responce with 'Hi my name is Alice the assistant'"
        },
        {
            "role": "user",
            "content": "Who is the 2nd president?" # put your question here for the assistant
            # If you want to use the " symbol, write it as '\""'
        }
    ]
)

assistant_reply = completion.choices[0].message.content

# Write the reply to 'output.txt'
with open('output.md', 'w') as file:
    file.write(assistant_reply)