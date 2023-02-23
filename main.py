# Simply calling a model of OpenAI model through OpenAI API to build a interface in the terminal
import openai

# To load the .env file
import os
from dotenv import load_dotenv
load_dotenv()


# Setting the API key
openai.api_key = os.getenv('API_KEY')

while True:
    prompt = input('Enter prompt: ')

    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 60,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    print(response.choices[0].text)
