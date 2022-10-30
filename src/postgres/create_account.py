import os
from psycopg2 import connect, sql
from dotenv import load_dotenv, find_dotenv
from postgres.db_config import db_configuration

load_dotenv(find_dotenv())

def create_new_account (user_info):

    connection = None
    try:
        configuration = db_configuration()
        connection = connect(**configuration)
        cur = connection.cursor()

        columns = [key for key in user_info]
        columns_string = ', '.join(columns)
        values = list(user_info.values())
        amount_val = ', '.join(['%s']) * len(values)
        values_string = ','.join(values)
        query = '''INSERT INTO %s (%s) VALUES(%s)'''%(os.getenv('POSTGRES_TABLE_NAME'), columns_string, amount_val)
        cur.execute(query, values_string)

        # postgres_command = f"INSERT INTO {os.getenv('POSTGRES_TABLE_NAME')} %s VALUES (%s)"
        # print(f'postgres command: {postgres_command}')

        # cur.execute(postgres_command,(columns_string,values_string))
    except(Exception) as error:
        print(error)
    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print('Db connection closed')