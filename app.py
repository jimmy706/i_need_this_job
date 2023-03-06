from flask import Flask, request, json
import openai
import os

app = Flask(__name__)


@app.post('/api/promote-letter')
def hello():
    return 'Hello, World!'

def generate_promote_letter():
    pass