import os

from psycopg2 import connect, sql
from dotenv import load_dotenv, find_dotenv
from postgres.db_config import db_configuration

load_dotenv(find_dotenv())

def create_new_account (user_info ):

    connection = None
    try:
        configuration = db_configuration()
        connection = connect(**configuration)
        cur = connection.cursor()
        table_name = os.getenv('POSTGRES_TABLE_NAME')

        values = tuple(user_info.values())

        insert_query_statement = sql.SQL("""
        INSERT INTO {tableName} 
        (first_name, middle_name, 
        last_name, gender, email,
        date_of_birth, 
        user_id, password)
        VALUES {values};
        """).format(tableName = sql.Identifier(table_name),values = sql.Literal(values))

        cur.execute(insert_query_statement)

        connection.commit()
        return 'User was successfully created'

    except(Exception) as error:
        print(error)
        return 'Unable to create account'
    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print('Db connection closed')