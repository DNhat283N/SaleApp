from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user



@app.route('/')
def index():
    keyword = request.args.get('key')
    cas = dao.get_categories()
    cat = request.args.get('cat')
    page = request.args.get('page')
    products = dao.get_products(keyword, cat, page)
    return render_template('index.html', categories=cas, products=products)


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)

    if user:
        login_user(user)

    return redirect('/admin')


@login.user_loader
def user_loader(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
