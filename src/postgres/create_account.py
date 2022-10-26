import os
import psycopg2

from dotenv import load_dotenv, find_dotenv
from postgres.db_config import db_configuration

load_dotenv(find_dotenv())

def create_account (user_info):

    connection = None
    try:
        configuration = db_configuration()
        connection = psycopg2.connection(**configuration)
        cur = connection.cursor()

        columns = [key for key in user_info]
        values = user_info.values()

        postgres_command = f"INSERT INTO {os.getenv('POSTGRES_TABLE_NAME')}({','.join(columns)})VALUES({','.join(values)})"

        cur.execute(postgres_command)
        pass
    except(Exception) as error:
        print(error)
    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print('Db connection closed')