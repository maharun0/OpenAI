# Import Flask and request module from Flask
from flask import Flask, request

# Import request
import requests

# Import AI response
from AI import get_AI_response

# Store records
from manage_records import set_records_in_csv

# access .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Access tokens & keys from .env file
FB_PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
WEBHOOK_VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

# create a Flask app instance
app = Flask(__name__)

def send_message(recipient_id, text):
    #"""Send a response to Facebook"""
    payload = {
        'message': {'text': text},
        'recipient': {'id': recipient_id},

        'notification_type': 'regular'
    }

    auth = {'access_token': FB_PAGE_ACCESS_TOKEN}

    response = requests.post(
        "https://graph.facebook.com/v2.6/me/messages?access_token={FB_PAGE_ACCESS_TOKEN}",
        params=auth,
        json=payload
    )

    return response.json()

# method to reply to a message from the sender
def reply(user_id, msg):
    response = get_AI_response(msg)
    set_records_in_csv(user_id, msg, response)
    send_message(user_id, response)

# GET request to handle the verification of tokens
@app.route('/', methods=['GET'])
def handle_verification():
    
    if request.args['hub.verify_token'] == WEBHOOK_VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"
        

# POST request to handle in coming messages then call reply()
@app.route('/', methods=['POST'])
def handle_incoming_messages():

    data = request.json
    #print ("\n"+data+"\n")

    try:
        sender = data['entry'][0]['messaging'][0]['sender']['id']
        message = data['entry'][0]['messaging'][0]['message']['text']

        reply(sender, message)
        
    # To handle multiple http calls at once
    except KeyError:
        print("One or more keys not found in data")
    except TypeError:
        print("Data is not in the expected format")

    return "ok"

# Run the application.
if __name__ == '__main__':
    app.run(debug=True) 
    