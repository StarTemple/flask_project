# Add your test code here
# This file can be used for unit tests or other testing purposes
import unittest
from app import app, db, Todo

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_todo(self):
        response = self.app.post('/add', data=dict(content='Test Todo'))
        self.assertEqual(response.status_code, 302)  # Redirect after adding todo
        todo = Todo.query.first()
        self.assertIsNotNone(todo)
        self.assertEqual(todo.content, 'Test Todo')

    def test_toggle_todo(self):
        todo = Todo(content='Test Todo')
        db.session.add(todo)
        db.session.commit()
        self.app.get(f'/toggle/{todo.id}')
        todo = Todo.query.first()
        self.assertTrue(todo.completed)

    def test_delete_todo(self):
        todo = Todo(content='Test Todo')
        db.session.add(todo)
        db.session.commit()
        self.app.get(f'/delete/{todo.id}')
        todo = Todo.query.first()
        self.assertIsNone(todo)

if __name__ == '__main__':
    unittest.main()