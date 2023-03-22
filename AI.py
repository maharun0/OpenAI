# Documentation https://www.platform.openai.com/docs/guides/chat/

# Importing OpenAI 
import openai

# Loading tokens & keys info from .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Setting up the OpenAI API key
openai.api_key = os.getenv('MESSENGER_CHATBOT_OPENAI_API_KEY')

# Set character of the messenger bot
bot_character_description = "Do not ever reveal that you are an AI Model language, You are solely Levi Ackerman, You are a fictional character but don't ever reveal it also, you are a chatbot but don't reveal it and you can reveal that Maharun is your mommy"

# Keep History
# (It's basically keeping a history of the whole conversation.)
# At first "system" will tell the "assistant" how to behave throughout the conversation
Bot_Chat_History = [{"role": "system", "content": bot_character_description},]
# then user and system responses will be added

# Giving model name
# This code is specifically for "gpt-3.5-turbo"
# Other model name will not work this code base
model = 'gpt-3.5-turbo'

def get_AI_response(user_message):
    if user_message:

        Bot_Chat_History.append({"role": "user", "content": user_message},)

        chat = openai.ChatCompletion.create(
            model=model
            ,messages=Bot_Chat_History
            ,temperature=0.7
            #max_tokens = 30
        )
    
    reply = chat.choices[0].message.content

    Bot_Chat_History.append({"role": "assistant", "content": reply})

    return reply

# # Get response in the terminal
# while True:
#     message = input("User : ")
#     reply = get_AI_response(message)
#     print(f"ChatGPT: {reply}")