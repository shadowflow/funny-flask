from db_object import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    # password = db.Column(db.String(15), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    valid = db.Column(db.Boolean, server_default='1')
    time = db.Column(db.DateTime, default=datetime.now())

    # author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # author = db.relationship('user', backref=db.backref('articles'))
