from app.models import Category, Product, User


def get_categories():
    return Category.query.all()


def get_products(key):
    products = Product.query
    if key:
        products = products.filter(Product.name.contains(key))

    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)