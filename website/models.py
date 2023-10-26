from . import db

# TodoItem model representing a table in the database
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000))
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TodoItem {self.id}>'