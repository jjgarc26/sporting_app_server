# we will use this main.py to create an endpoint to receive information needed for postgres
import json

from flask import Flask
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
        response = app.response_class (
            response= json.dumps(verification),
            status=200,
            mimetype='application/json'
        )
    except(Exception) as error:
        response = app.response_class (
            response= f'error has occurred: {error}',
            status=400,
            mimetype='application/json' 
        )
    
    return response

