from flask import render_template

from app import app
from app.models.orders_app import orders

@app.route('/orders')
def index():
    return render_template(
        'index.html',
        title = 'Better Than Amazon', 
        orders = orders)

@app.route('/orders/<index>')
def ordered(index):
    return render_template(
        'order.html',
        index = index,
        orders = orders,
        ind_num = int(index)
        

        )

