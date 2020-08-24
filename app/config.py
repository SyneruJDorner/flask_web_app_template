  
import os, sys, json

class Config:
    json_file=None
    data = None

    with open('app/secret_info/secret_info.json') as json_file:
        data = json.load(json_file)

    if (data == None):
        print("Unable to load in the correct data from the json file located in 'app/secret_info/secret_info.json'")
        print("Otherwise please use the 'app/secret_info/secret_info_example.json' to create the 'app/secret_info/secret_info.json', and just fill in your info needed.")
        sys.exit()

    SECRET_KEY = data['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = data['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = data['MAIL_USERNAME']
    MAIL_PASSWORD = data['MAIL_PASSWORD']
