from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI','sqlite:///todo.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('DB_TRACK_MODIFICATIONS',False)
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/init")
def init():
    db.create_all()
    data = {'app': 'Todo List App','version': '1.0','db': 'initialized'}
    return jsonify(data), 200

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/health")
def health():
    db.engine.execute('SELECT 1')
    data = {'app': 'Todo List App','version': '1.0','health': 'ok'}
    return jsonify(data), 200

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
