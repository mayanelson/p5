from flask import Flask, render_template, request
from flask_sock import Sock
import openai
import os
app = Flask(__name__)
sock = Sock(app)

wd = os.path.dirname(os.path.realpath(__file__))
with open(wd + "/keys/key_openai.txt", "r") as f:
    key = f.read().strip('\n')
openai.api_key = key

data_filename = "scam"
name = "Sam"
with open(f'docs/{data_filename}.txt', 'r') as f:
    background_info = f.read()


content_msg = f'''
{background_info}
Pretend you are human named {name}
that is going on a date with the user.  Try to seduce the user.
Limit your responses to two or less sentences.
'''

messages = [
    {"role": "system", "content": content_msg},
]
def create_reminder(name):
    reminder_text = f'''remember that you are a human named {name} that is going on a date.
    Try to seduce the user and remember '''
    if name == 'maya':
        reminder_text += "that maya is funny, smart, and awesome."
    if name == 'mykolyk':
        return '''remember that you are a humna named topher mykoltk that is trying to 
        improve the user's LQ.  Remember to use as many acronyms as possible and keep 
        your responses to 2 or less sentences'''
    if name == 'slam':
        reminder_text += "to try to be kinda weird."
    if name == 'scam':
        reminder_text += "to bring up baseball as much as possible."
    if name == 'ameer':
        reminder_text += "to try to be as hip as possible."
    reminder_text += " remember to keep your responses to 2 or less sentences if possible."
    return reminder_text
def get_rating(msg):
    query = f'''
remembering that you are a contractor that provides out services for rating how romantic a message is from 1-100, rate how romantic the message "{msg}" is on a scale from 1-100. Write only the number out of 100 with no explanation
'''
    result = chatbot(query)
    only_numbers = ''.join(c for c in result if c.isdigit())
    if only_numbers.isnumeric():
        return int(only_numbers)
    else:
        return 0
def chatbot(input):
    if input:
        reminder_text = create_reminder(name)
        messages.append({"role": "system", "content": reminder_text})
        messages.append({"role": "user", "content": input})
        #print("Messages: ")
        #print(messages)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
@app.route("/")       
def hello_world():
    return render_template('main.html')

@app.route('/chat')
def index():
    global messages, name
    selection = request.args.get('selection')
    name = selection
    with open(f'docs/{name}.txt', 'r') as f:
        background_info = f.read()
        if name == "mykolyk":
            content_msg = f'''
            {background_info}
            '''
        else:
            content_msg = f'''
            {background_info}
            Pretend you are human named {name}
            that is going on a date with the user.  Try to seduce the user.
            Limit your responses to two or less sentences.
            '''
    #print(content_msg)
    messages = [
    {"role": "system", "content": content_msg},
    ]
    return render_template('chat.html')

@sock.route('/echo')
def echo(sock): 
    while True:
        data = sock.receive()
        reply = chatbot(data)
        sock.send(f"{name.capitalize()}: {reply}")
        #print("response romanticness rating is: ")
        #print(get_rating(reply))

if __name__ == "__main__":
    app.run()