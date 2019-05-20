from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps
from flask import request

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pyintro"
mongo = PyMongo(app)


@app.route("/")
def home_page():
    return jsonify("Hi!", "GET /user/<id>", "POST /user/", "PUT /user/<id>")


@app.route("/user/<ObjectId:id>")
def user_get(id):
    result = mongo.db.peeps.find_one_or_404({"_id": id})
    return dumps(result)


@app.route("/user", methods=["POST"])
def user_create():
    user = request.get_json()
    result = mongo.db.peeps.insert_one(user).inserted_id
    return dumps(result)


@app.route("/user/<ObjectId:id>", methods=["PATCH"])
def user_patch(id):
    fields_to_set = request.get_json()
    result = mongo.db.peeps.update_one({"_id": id}, {"$set": fields_to_set})

    return update_result(result)


@app.route("/user/<ObjectId:id>/likes", methods=["PUT"])
def user_add_likes(id):
    items = request.get_json()
    result = mongo.db.peeps.update_one(
        {"_id": id}, {"$addToSet": {"likes": {"$each": items}}}
    )

    return update_result(result)


@app.route("/user/<ObjectId:id>/likes", methods=["DELETE"])
def user_remove_likes(id):
    items = request.get_json()
    result = mongo.db.peeps.update_one({"_id": id}, {"$pullAll": {"likes": items}})

    return update_result(result)

@app.route("/user/<ObjectId:id>/fields/<string:field>", methods=["DELETE"])
def user_remove_field(id, field):
    expr = {}
    expr[field] = True
    result = mongo.db.peeps.update_one({"_id": id}, {"$unset": expr})

    return update_result(result)

def update_result(write_result):
    raw = dumps(write_result.raw_result)

    if write_result.matched_count == 0:
        return raw, 404

    if write_result.modified_count == 0:
        return raw, 304

    if write_result.modified_count == 1:
        return raw, 200

