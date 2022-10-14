import json


def verify_user(user_information):
    # user_info = json.load(user_information)
    # print(user_info['username'])
    verify_username = user_information['username']
    verify_password = user_information['password']
    return verify_username