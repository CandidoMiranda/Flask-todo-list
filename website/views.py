from flask import render_template, request, redirect, url_for,  Blueprint
from .models import TodoItem
from . import db

views = Blueprint('views', __name__)

@views.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # Creating a new TodoItem object and adding it to the database
        content = request.form['content']
        if content.strip() != '':
            new_item = TodoItem(content=content)
            db.session.add(new_item)
            db.session.commit()
        return redirect('/')
    else:
        # Querying all TodoItem objects from the database and redering the template
        items = TodoItem.query.all()
        return render_template('index.html', items=items)

@views.route('/complete/<int:item_id>')
def complete(item_id):
    # Retrieving a TodoItem object by ID, making it as completed, and commiting the changes
    item = TodoItem.query.get_or_404(item_id)
    item.completed = True
    db.session.commit()
    return redirect('/')

@views.route('/delete/<int:item_id>')
def delete(item_id):
    # Retrieving a TodoItem object by ID, deleting it, and commiting the changes
    item = TodoItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

