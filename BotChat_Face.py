from flask import Flask, request
import requests

app = Flask(__name__)

FACEBOOK_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = '<https://www.facebook.com/profile.php?id=100034358779961>'
PAGE_ACCESS_TOKEN = '<https://www.facebook.com/profile.php?id=100034358779961>'

@app.route('/', methods=['GET'])
def verify_webhook():
    if request.args.get('hub.verify_token') == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    else:
        return 'Invalid request or verification token'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                if 'message' in messaging_event:
                    message_text = messaging_event['message']['text']
                    send_message(sender_id, message_text)
    return 'OK'

def send_message(recipient_id, text):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'messaging_type': 'RESPONSE',
        'recipient': {
            'id': recipient_id,
        },
        'message': {
            'text': text,
        }
    }
    params = {
        'access_token': PAGE_ACCESS_TOKEN,
    }
    response = requests.post(FACEBOOK_API_URL, headers=headers, params=params, json=data)
    response.raise_for_status()

if __name__ == '__main__':
    app.run(port=5000)
