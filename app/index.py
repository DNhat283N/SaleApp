from flask import render_template, request
import dao
from app import app, login


@app.route('/')
def index():
    keyword = request.args.get('key')
    cas = dao.get_categories()
    products = dao.get_products(keyword)
    return render_template('index.html', categories=cas, products=products)


@login.user_loader
def user_loader(user_id):
    dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
