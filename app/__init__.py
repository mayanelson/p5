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

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        print("Messages: ")
        print(messages)
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
    print(content_msg)
    messages = [
    {"role": "system", "content": content_msg},
    ]
    return render_template('chat.html')

@sock.route('/echo')
def echo(sock): 
    while True:
        data = sock.receive()
        sock.send(f"{name.capitalize()}: {chatbot(data)}")

if __name__ == "__main__":
    app.run()