import math

from flask import render_template, request, redirect, jsonify, session
import dao
import utils
from app import app, login
from flask_login import login_user


@app.route('/')
def index():
    keyword = request.args.get('key')
    cat = request.args.get('cat')
    page = request.args.get('page')
    number_of_products = dao.count_product()
    page_size = app.config['PAGE_SIZE']
    products = dao.get_products(keyword, cat, page)
    return render_template('index.html', products=products,
                           pages=math.ceil(number_of_products/page_size))


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)

    if user:
        login_user(user)

    return redirect('/admin')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/api/cart', methods=['post'])
def add_to_cart():
    data = request.json
    cart = session.get('cart')
    if cart is None:
        cart = {}
    id = str(data.get('id'))
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }
    session['cart'] = cart
    return jsonify(utils.count_cart(cart))


@app.context_processor
def common_response():
    return {
        'categories': dao.get_categories(),
        'cart_stats': utils.count_cart()
    }


@login.user_loader
def user_loader(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
