from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Todo %r>' % self.id

# Route to display all todos
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)