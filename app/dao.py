from app.models import Category, Product, User
from app import app
import hashlib


def get_categories():
    return Category.query.all()


def get_products(key, cat, page = None):
    products = Product.query
    if key:
        products = products.filter(Product.name.contains(key))
    if cat:
        products = products.filter(Product.category_id.contains(cat))
    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1) * page_size
        return products.slice(start, start + page_size)

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
