from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import Relationship


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = Relationship('Product', backref="category", lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://cdn1.viettelstore.vn/Images/Product/ProductImage/213191152.jpeg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')
        c3 = Category(name='Laptop')

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)

        db.session.commit()

        p1 = Product(name='iPhone 13', price=20000000, category_id=1)
        p2 = Product(name='iPhone 13 Pro', price=23000000, category_id=1)
        p3 = Product(name='iPhone 13 Pro Max', price=27000000, category_id=1)
        p4 = Product(name='Galaxy S23', price=18000000, category_id=1)
        p5 = Product(name='iPad Pro 2023', price=21000000, category_id=2)

        db.session.add_all(p1, p2, p3, p4, p5)
        db.session.commit()


