import os

from psycopg2 import connect, sql
from dotenv import load_dotenv, find_dotenv
from postgres.configs.db_configuration import db_configuration

load_dotenv(find_dotenv())

def update_login_password(new_password_info):
    connection = None
    try:
        configuration = db_configuration()
        connection = connect(**configuration)
        cur = connection.cursor()
        table_name = os.getenv('POSTGRES_TABLE_NAME')
        
        user_id = new_password_info['userId']
        new_password = new_password_info['newPassword']
        
        update_query_statement = sql.SQL("""
        UPDATE {tableName}
        SET password = {newPassword}
        WHERE user_id = {userId}
        """).format(tableName = sql.Identifier(table_name), newPassword = sql.Literal(new_password), userId = sql.Literal(user_id))

        cur.execute(update_query_statement)

        connection.commit()
        return 'Password has been updated'
    except(Exception) as error:
        print(f"Error has occurred: {error}")
        return f"Unable to update password"
    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print('Db connection closed')