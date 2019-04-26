from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pyintro"
mongo = PyMongo(app)

@app.route('/')
def home_page():
    return jsonify('hello', 'world!')

@app.route("/user/<username>")
def user_profile(username):
    result = mongo.db.peeps.find_one_or_404({"name": username})
    return dumps(result)




