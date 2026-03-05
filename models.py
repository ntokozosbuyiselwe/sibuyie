from models import all
from flask_sqlalchemy import SQLAlchemy
from app import db


class user():
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.string(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

class Book():
    b_id=int()#cascade delete if user is 
    b_name=str(max=500, null=False)
    b_price=float()
    b_quantity=int()


class cart():
    id = int ()#

