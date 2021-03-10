from flask import render_template

from app import app
from app.models.todo_list import orders

@app.route('/orders')
def index():
    return render_template(
        'index.html',
        title = 'Better Than Amazon', 
        orders = orders)