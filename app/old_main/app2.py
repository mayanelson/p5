import gradio as gr
import sys
import os
from abc import ABC, abstractmethod
from typing import List
from langchain.schema import Document
import chromadb
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

wd = os.path.dirname(os.path.realpath(__file__))
file = open(wd + "/keys/key_openai.txt", "r")
openaiKey = file.read()
#print(openaiKey)
file.close()

os.environ["OPENAI_API_KEY"] = openaiKey



class BaseRetriever(ABC):
    @abstractmethod
    def get_relevant_documents(self, query: str) -> List[Document]:
        """Get texts relevant for a query.

        Args:
            query: string to find relevant texts for

        Returns:
            List of relevant documents
        """

loader = TextLoader('docs/sam_description.txt', encoding='utf8')
index = VectorstoreIndexCreator().from_loaders([loader])
global query

query = "Pretend you are Sam Cowan\nYou are going on a date with the user.  Try to seduce the user, and\nanswer the user's questions in first person as Sam Cowan. Keep your responses to two sentences or less. \nUser:"

def tester(input):
    if input:
        print(query)
        query += input
        print(query)


def chatbot(input):
    if input:
        #nonlocal query
        global query
        query += input
        reply = index.query_with_sources(query + input)
        query += "\n AI: " + reply['answer'] + "\n User:"
        print(query)
        return reply['answer']

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)