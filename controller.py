from nlp import witprocess
import json 
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('definitions.json') as fr:    
    definitions = json.load(fr)

@app.route('/')
def home():
    return '<h1>Online</h1>'

@app.route('/process', methods=['GET'])
def process():
    input = request.args.get('input')
    response = witprocess.recievemessage(input)
    response['definition'] = definitions[response['word']]['defi']
    response['link'] = definitions[response['word']]['mention']['term']
    response['reference'] = definitions[response['word']]['mention']['link']
    return jsonify(response)

if __name__ == "__main__":
  app.run()