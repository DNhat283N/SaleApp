from flask import render_template, request
import dao
from app import app


@app.route('/')
def index():
    keyword = request.args.get('key')
    cas = dao.get_categories()
    products = dao.get_products(keyword)
    return render_template('index.html', categories=cas, products=products)


if __name__ == '__main__':
    app.run(debug=True)
