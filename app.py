import os
from flask import Flask
import flask_pymongo
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://carlvinggaard:18M0n90d603@cluster0-lqr5z.mongodb.net/task_manager?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def home_page():
    post = {"is_urgent": True, "task_name": "Pick up the kids"}
    mongo.db.tasks.insert_one(post)
    return "Post inserted." 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
