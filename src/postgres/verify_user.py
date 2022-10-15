import json
import os
import psycopg2

from dotenv import load_dotenv, find_dotenv
from postgres.db_config import db_configuration

load_dotenv(find_dotenv())

def query_db(username):

    connection = None
    try:
        configurations = db_configuration()
        connection = psycopg2.connect(**configurations)
        cur = connection.cursor()

        postgres_query_command = f"SELECT user_id, password from {os.getenv('POSTGRES_TABLE_NAME')} WHERE user_id = %s"
        
        cur.execute(postgres_query_command,(username,))
        user = cur.fetchall()

        user_credentials = {
            'username': '',
            'password': ''
        }

        for row in user:
            user_credentials['username'] = row[0]
            user_credentials['password'] = row[1]
        
        print(user_credentials)
        return user_credentials

    except (Exception, psycopg2.Error) as error:
        print('An error has occurred', error)

    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print('Db connection closed')


def verify_user(user_information):
    verify_username = user_information['username']
    verify_password = user_information['password']

    verify_user = {
        'username' : verify_username,
        'password' : verify_password
    }

    user = query_db(username=verify_user['username'])
    print(user)
    if user['username'] is not '':
        return 'User verified'
    else:
        return 'User does not exist'
    

