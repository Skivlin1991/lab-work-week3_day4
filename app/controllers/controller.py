from flask import render_template

from app import app
from app.models.orders_app import orders

@app.route('/orders')
def index():
    return render_template(
        'index.html',
        title = 'Better Than Amazon', 
        orders = orders)

