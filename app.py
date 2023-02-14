from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite database for managing to-do tasks using the SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initializing this app with SQLAlchemy database
db = SQLAlchemy(app)


# Model class for to-do tasks which includes the ID, name and status of the tasks
class Todo(db.Model):
    todo_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    status_done = db.Column(db.Boolean)


# Defining the behaviour of the app on '/' endpoint.
# All the tasks will be rendered in a tabular form on homepage.
@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)


# Adding a new record on when '/add' endpoint is hit.
# Changes to the database and the display table is are made simultaneously.
@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    new_task = Todo(name=name, status_done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))


# Updating the status of the record when '/status_changes' endpoint is hit.
# Changes to the database and the display table are made simultaneously.
# NOTE: Record ID is required to update the status of a record.
@app.route('/status/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get(todo_id)
    todo.status_done = not todo.status_done
    db.session.commit()
    return redirect(url_for('home'))


# Updating the task when '/update' endpoint is hit.
# Changes to the database and the display table are made simultaneously.
# NOTE: Record ID is required to delete a record.
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    # When the user is updating a record, this endpoint is hit with a 'POST' request from the 'update' page.
    # User provides the 'todo_id' in order to make changes to that very record.
    if request.method == 'POST':
        name = request.form.get('name')
        todo = Todo.query.get(todo_id)
        todo.name = name
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))

    todo = Todo.query.get(todo_id)
    return render_template('update.html', todo=todo)


# Deleting the task when '/delete' endpoint is hit.
# Changes to the database and the display table are made simultaneously.
# NOTE: Record ID is required to delete a record.
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
