from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

main = Flask(__name__)
db = SQLAlchemy
main.config['SQUALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
main.config['SECRET_KEY'] = 'thisisasecretkey'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullabl=False)
    password = db.Column(db.String(20), nullabl=False)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    main.run(debug=True)
