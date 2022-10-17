# we will use this main.py to create an endpoint to receive information needed for postgres
import json

from flask import Flask, request
from flask_cors import CORS
from postgres.verify_user import verify_user

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '<p>Hello</p>'

@app.route('/login/<username>', methods=['GET'])
def login(username):
    try:
        print(username)
        verification = verify_user(username)
        response = json.dump(verification)
    except(Exception) as error:
        print(error)
    
    return response

