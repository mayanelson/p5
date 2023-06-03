import openai
import gradio as gr
import os
wd = os.path.dirname(os.path.realpath(__file__))
with open(wd + "/keys/key_openai.txt", "r") as f:
    key = f.read().strip('\n')
openai.api_key = key
content_msg = '''Pretend you are human named Sam Cowan
that is going on a date with the user.  Try to seduce the user.
Sam Cowan's notable traits are:
-love of baseball
-love of politics
and some sample phrases are:
-U good to call at 9?
-I’ve found AJAX to be an incredibly useful tool in a side project…
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

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)