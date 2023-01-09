from dotenv import load_dotenv, find_dotenv
from configparser import ConfigParser

load_dotenv(find_dotenv())
file = 'configs/database.ini'

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
