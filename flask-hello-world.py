"""

+=== BASIC INFO ===+
-- October 30, 2021
-- Rahul Goel
-- Learning buidling a REST API in Flask

+=== RESOURCES ===+
-- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

"""


# Import requirements
from flask import Flask
from flask import jsonify

# Setup Flask
app = Flask(__name__)]


# A simple Hello world 
@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

# A simple Goodbye world
@app.route("/bye")
def goodbye_world():
    return "<h2> Goodbye, my flasky friend!</h2>"


