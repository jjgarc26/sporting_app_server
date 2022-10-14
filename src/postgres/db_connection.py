import psycopg2
from configparser import ConfigParser

file = '../configs/database.ini'
def db_configuration(filename=file, section='postgresql'):

    parser = ConfigParser()

    parser.read(filename)

    database_information = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database_information[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename}")
    
    print(database_information)
    return database_information


def connect_to_db():
    
    connection = None

    try:
        configurations = db_configuration()
        connection = psycopg2.connect(**configurations)

        cur = connection.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        return db_version
        cur.close()

    except:
        print('An error has occurred')
    finally:
        if connection is not None:
            connection.close()
            print('Db connection closed')

connect_to_db()

# if __name__ == '__main__':
#     connect_to_db()