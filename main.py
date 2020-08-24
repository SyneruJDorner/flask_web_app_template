#pip install flask
#pip install flask-wtf
#pip install email_validator
#pip install flask-sqlalchemy
#pip install flask-bcrypt
#pip install flask-login
#pip install pillow
#pip install flask-mail

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)