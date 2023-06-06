from flask import Flask, render_template
from flask_sock import Sock
import openai
import os
app = Flask(__name__)
sock = Sock(app)

wd = os.path.dirname(os.path.realpath(__file__))
with open(wd + "/keys/key_openai.txt", "r") as f:
    key = f.read().strip('\n')
openai.api_key = key

data_filename = "sam_description"
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
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

@app.route('/')
def index():
    return render_template('index.html')

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send("Sam: " + chatbot(data))

if __name__ == "__main__":
    app.run()