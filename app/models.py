from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import click
from flask import current_app, Blueprint
from app import db, bcrypt, login_manager
from pathlib import Path
from flask_login import UserMixin
from flask.cli import AppGroup

#region Model Functions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#endregion


#region Model Classes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
#endregion


#region Model Commands
commands_cli = AppGroup('commands')

#flask commands db_create
@commands_cli.command(name='db_create', help="Creates a database.")
def db_create():
    Path("app/Databases").mkdir(parents=True, exist_ok=True)
    db.create_all()
    print('Database created!')

#flask commands db_drop
@commands_cli.command(name='db_drop', help="Drops a database.")
def db_drop():
    db.drop_all()
    print('Database dropped!')

#flask commands db_seed
@commands_cli.command(name='db_seed', help="Seeds a database.")
def db_seed():
    hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')

    user_1 = User(username='Justin', email='justin@test.com', password=hashed_password)
    user_2 = User(username='Morne', email='morne@test.com', password=hashed_password)
    user_3 = User(username='Happy', email='happy@test.com', password=hashed_password)
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.add(user_3)
    db.session.commit()

    post_1 = Post(title='Blog_1', content='1st Post Content!', user_id=user_1.id)
    post_2 = Post(title='Blog_2', content='2nd Post Content!', user_id=user_2.id)
    post_3 = Post(title='Blog_3', content='3rd Post Content!', user_id=user_3.id)
    post_4 = Post(title='Blog_4', content='4th Post Content!', user_id=user_1.id)
    post_5 = Post(title='Blog_5', content='5th Post Content!', user_id=user_2.id)
    post_6 = Post(title='Blog_6', content='6th Post Content!', user_id=user_3.id)
    post_7 = Post(title='Blog_7', content='7th Post Content!', user_id=user_1.id)
    post_8 = Post(title='Blog_8', content='8th Post Content!', user_id=user_2.id)
    post_9 = Post(title='Blog_9', content='9th Post Content!', user_id=user_3.id)
    post_10 = Post(title='Blog_10', content='10th Post Content!', user_id=user_1.id)
    post_11 = Post(title='Blog_11', content='11th Post Content!', user_id=user_2.id)
    post_12 = Post(title='Blog_12', content='12th Post Content!', user_id=user_3.id)
    post_13 = Post(title='Blog_13', content='13th Post Content!', user_id=user_1.id)
    post_14 = Post(title='Blog_14', content='14th Post Content!', user_id=user_2.id)
    post_15 = Post(title='Blog_15', content='15th Post Content!', user_id=user_3.id)
    post_16 = Post(title='Blog_16', content='16th Post Content!', user_id=user_1.id)
    post_17 = Post(title='Blog_17', content='17th Post Content!', user_id=user_2.id)
    post_18 = Post(title='Blog_18', content='18th Post Content!', user_id=user_3.id)
    post_19 = Post(title='Blog_19', content='19th Post Content!', user_id=user_1.id)
    post_20 = Post(title='Blog_20', content='20th Post Content!', user_id=user_2.id)
    post_21 = Post(title='Blog_21', content='21st Post Content!', user_id=user_3.id)
    post_22 = Post(title='Blog_22', content='22nd Post Content!', user_id=user_1.id)
    post_23 = Post(title='Blog_23', content='23rd Post Content!', user_id=user_2.id)
    post_24 = Post(title='Blog_24', content='24th Post Content!', user_id=user_3.id)
    post_25 = Post(title='Blog_25', content='25th Post Content!', user_id=user_1.id)

    db.session.add(post_1)
    db.session.add(post_2)
    db.session.add(post_3)
    db.session.add(post_4)
    db.session.add(post_5)
    db.session.add(post_6)
    db.session.add(post_7)
    db.session.add(post_8)
    db.session.add(post_9)
    db.session.add(post_10)
    db.session.add(post_11)
    db.session.add(post_12)
    db.session.add(post_13)
    db.session.add(post_14)
    db.session.add(post_15)
    db.session.add(post_16)
    db.session.add(post_17)
    db.session.add(post_18)
    db.session.add(post_19)
    db.session.add(post_20)
    db.session.add(post_21)
    db.session.add(post_22)
    db.session.add(post_23)
    db.session.add(post_24)
    db.session.add(post_25)

    db.session.commit()

    print('Database seeded!')

#flask commands db_user_query
@commands_cli.command(name='db_user_query', help="Queries all users.")
def db_user_query():
    print(User.query.all())

#flask commands db_user_query_by_username --username justin
@commands_cli.command(name='db_user_query_by_username', help="Queries all users with the specified username.")
@click.option("--username")
def db_user_query_by_username(username):
    print(User.query.filter_by(username=username).all())
#endregion