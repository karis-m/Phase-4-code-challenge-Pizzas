from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Restaurant model
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurantPizza.restaurant',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    address = db.Column(db.String)

    pizzas = db.relationship('RestaurantPizza', back_populates = 'pizza')

    def __repr__(self):
        return f'<Restaurant {self.name} for {self.address}>'
    
# Pizza model
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurantPizza.pizza',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    ingredients = db.Column(db.String)

    restaurant = db.relationship('RestaurantPizza', back_populates = 'restaurant')

    def __repr__(self):
        return f'<Pizza {self.name} for {self.ingredient}>'
    
# RestaurantPizza relational model

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    serialize_rules = ('-pizza.restaurantPizza', '-restaurant.restaurantPizza')

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
   
    # relationships
    restaurant = db.relationship('Restaurant', back_populates='pizza')
    pizza = db.relationship('Pizza', back_populates='restaurant')

    def __repr__(self):
        return f'<Restaurant Pizza {self.restaurant} for {self.price}>'