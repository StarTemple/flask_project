# This file can be used for additional functionality related to todo items
# For example, you can add functions to handle more complex business logic
from app import db, Todo

def get_all_todos():
    return Todo.query.all()

def add_todo(content):
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()

def toggle_todo_completion(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = not todo.completed
    db.session.commit()

def delete_todo_by_id(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()