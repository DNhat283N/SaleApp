from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Enum, DateTime
from sqlalchemy.orm import Relationship
from flask_login import UserMixin
import enum
from datetime import datetime


class UserRoleEnum(enum.Enum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), default='https://cdn1.viettelstore.vn/Images/Product/ProductImage/213191152.jpeg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    receipts = Relationship('Receipt', backref="user", lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = Relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://cdn1.viettelstore.vn/Images/Product/ProductImage/213191152.jpeg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    receipt_details = Relationship('ReceiptDetails', backref="product", lazy=True)

    def __str__(self):
        return self.name


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    createdDate = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)


class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    receipt_details = Relationship('ReceiptDetails', backref='receipt', lazy=True)


class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib

        u1 = User(name='Admin', username='admin', password=str(hashlib.md5('12345'.encode('utf-8')).hexdigest()), user_role=UserRoleEnum.ADMIN)
        db.session.add(u1)
        db.session.commit()

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

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
