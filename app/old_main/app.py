'''Sam Cowan's notable traits are:
-love of baseball
-love of politics
and some sample phrases are:
-U good to call at 9?
-I’ve found AJAX to be an incredibly useful tool in a side project…'''
import openai
import gradio as gr
import os
from flask import Flask, render_template
app = Flask(__name__)
data_filename = "sam_description"
wd = os.path.dirname(os.path.realpath(__file__))
with open(wd + "/keys/key_openai.txt", "r") as f:
    key = f.read().strip('\n')
with open(f'docs/{data_filename}.txt', 'r') as f:
    background_info = f.read()
openai.api_key = key
name = "Maya"
content_msg = f'''
{background_info}
Pretend you are human named {name}
that is going on a date with the user.  Try to seduce the user.
Limit your responses to two or less sentences.
'''
messages = [
    {"role": "system", "content": content_msg},
]
@app.route("/")
def chat():
    selection = request.args.get('selection')
    return render_template('chat.html', selection=selection)
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)