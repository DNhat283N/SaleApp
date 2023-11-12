from app.models import Category, Product


def get_categories():
    return Category.query.all()


def get_products(key):
    products = Product.query
    if key:
        products = products.filter(Product.name.contains(key))

    return products.all()
