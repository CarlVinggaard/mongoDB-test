import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://carlvinggaard:18M0n90d603@cluster0-lqr5z.mongodb.net/task_manager?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find()) 


@app.route('/add_task')
def add_tasks():
    return render_template('addtasks.html', categories=mongo.db.categories.find()) 


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
