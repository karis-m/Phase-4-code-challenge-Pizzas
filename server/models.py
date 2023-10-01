from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Restaurant model
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    address = db.Column(db.String)

    pizzas = db.relationship('RestaurantPizza', back_populates = 'pizza')

# Pizza model
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    ingredients = db.Column(db.String)

    restaurant = db.relationship('RestaurantPizza', back_populates = 'restaurant')

# RestaurantPizza relational model

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    price = db.Column(db.Integer)
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
   
    # relationships
    restaurant = db.relationship('Restaurant', back_populates='pizza')
    pizza = db.relationship('Pizza', back_populates='restaurant')