from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from generator import *

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return "Article Genarator Using Gemini AI"

@app.route('/generate', methods=['GET','POST'])
def articles():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        description = get_description(keyword)
        content = get_article(keyword)
        image = get_image(keyword)
        result = {
            'description': description,
            'content': content,
            'image': image
        }
        return make_response(jsonify(result)), 200
    else:
        response = {
            'message': 'Use POST Method & Entry keyword'
        }
        return make_response(jsonify(response)), 200

@app.route('/generator/<keyword>', methods=['GET'])
def generator(keyword):
    if request.method == 'GET':
        description = get_description(keyword)
        content = get_article(keyword)
        image = get_image(keyword)
        result = {
            'description': description,
            'content': content,
            'image': image
        }
        return make_response(jsonify(result)), 200
    else:
        response = {
            'message': 'Use GET Method'
        }
        return make_response(jsonify(response)), 200