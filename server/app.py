from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/restaurants')
def get_restaurant():
    restaurants = []
    
    for restaurant in Restaurant.query.all():
       restaurant_dict = {
          "id" : restaurant.id,
          "name" : restaurant.name,
          "address" : restaurant.address
       }
       restaurants.append(restaurant_dict)
    
    response = make_response(jsonify(restaurants), 200)

    return response

@app.route('/restaurants/<int:id>', methods = ['GET', 'DELETE'])
def restaurantById(id):
    restaurant = Restaurant.query.filter_by(id=id).First()
    
    if restaurant == None:
        response_body = {
            "error": "Restaurant not found"
        }
        response = make_response(jsonify(response_body))
        return response
    
    else:
        if request.method == 'GET':
         restaurant_dict = Restaurant.query.filter_by(id=id).first().to_dict()
         response = make_response(jsonify(restaurant_dict))
         
         return response
        
        elif request.method == 'DELETE':
           restaurant_pizza = RestaurantPizza.query.filter_by(restaurant_id=id).first()
           db.session.delete(restaurant_pizza)
           db.session.commit()

           restaurant = Restaurant.query.filter_by(id=id).first()
           db.session.delete(restaurant)
           db.session.commit()
           
           response_body = {
                "delete_successful": True,
                "message": "Message deleted."    
            }
           response = make_response(jsonify(response_body), 200)
           
           return response

@app.route('/pizzas')
def get_pizzas():
    pizzas = []
    
    for pizza in Pizza.query.all():
       pizza_dict = {
          "id" : pizza.id,
          "name" : pizza.name,
          "ingredients" : pizza.ingredients
       }
       pizzas.append(pizza_dict)
    
    response = make_response(jsonify(pizzas), 200)

    return response
    
@app.route('/restaurant_pizzas', methods = ['POST'])
def post_restaurant_pizzas():
    if request.method == 'POST':
        new_restaurant_pizza = RestaurantPizza(
           price = request.form.get("price"),
           pizza_id = request.form.get("pizza_id"),
           restaurant_id = request.form.get("restaurant_id"),
         )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        response_to_dict = new_restaurant_pizza.to_dict()
        response = make_response(jsonify(response_to_dict), 201)

        return response