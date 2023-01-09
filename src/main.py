# we will use this main.py to create an endpoint to receive information needed for postgres
import json

from flask import Flask, request
from flask_cors import CORS
from postgres.verify_user import verify_user
from postgres.create_account import create_new_account
from postgres.update_password import update_login_password

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
@app.route('/update_password',methods=['POST'])
def update_password():
    try:
        new_password_info = request.get_json()
        updated_password = update_login_password(new_password_info)
        response = app.response_class(
            response=json.dumps(updated_password),
            status=200,
            mimetype='application/json'
        )
    except(Exception) as error:
        response = app.response_class(
            response = f'error has occurred: {error}',
            status=400,
            mimetype='application/json'
        )
    return response
@app.route('/create_account', methods=['POST'])
def create_account():
    try:
        new_account_info = request.get_json()
        create = create_new_account(new_account_info)
        response = app.response_class(
            response= json.dumps(create),
            status=200,
            mimetype='application/json'
        )
        
    except(Exception) as error:
        response = app.response_class(
            response = f'error has occurred: {error}',
            status=400,
            mimetype='application/json'
        )
    return response



