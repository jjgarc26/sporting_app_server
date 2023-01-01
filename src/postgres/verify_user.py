import json
import os

from psycopg2 import connect, sql
from dotenv import load_dotenv, find_dotenv
from postgres.db_config import db_configuration

load_dotenv(find_dotenv())

def verify_user(username):

    connection = None
    try:
        # set connection up for db
        configurations = db_configuration()
        connection = connect(**configurations)
        cur = connection.cursor()
        table_name = os.getenv('POSTGRES_TABLE_NAME')

        #creates select query statement for DB
        select_query_statement = sql.SQL("""
        SELECT user_id, password 
        from {tableName}
        WHERE user_id = {userId};
        """).format(tableName = sql.Identifier(table_name), userId = sql.Literal(username))

        cur.execute(select_query_statement)
        user = cur.fetchall()

        user_credentials = {
            'username': '',
            'password': ''
        }

        for row in user:
            user_credentials['username'] = row[0]
            user_credentials['password'] = row[1]
        
        response = {}
        if user_credentials['username'] != '':
            response['response'] = 'user is verified'

        else:
            response['response'] = 'user is not verified'
        return response

    except (Exception) as error:
        print('An error has occurred', error)

    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print('Db connection closed')

    

