from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Gemini Article Generator'

@app.route('/api')
def api():
    api_key = os.getenv("API_KEY")
    return api_key