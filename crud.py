from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallopw import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'crud.sqlite')
db=SQAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


    def __init__(self, username, email):         self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

# endpoint to create a new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()


    return jsonify(new_user)

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["PUT"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)



