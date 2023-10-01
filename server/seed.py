#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app

from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

restaurant_name = [
    "Big Bang Hotel",
    "Cupcake Hotel",
    "Less Hotel",
    "The May Day",
    "Bad Ass Hotel",
    "Red Box Hotel",
    "Snooze Lodge",
    "Vagabond Cabin",
    "Voltage Hotel",
    "Raspberry Hotel",
    "Roam Cabin",
]
ingredients  = [
    "Broccolini or broccoli (blanch first) and pancetta/speck/bacon.",
    "Potato, sausage, pancetta/speck/bacon.",
    "Gorgonzola and mushroom.",
    "Black olives, anchovies, capers.",
    "Gorgonzola, radicchio.",
    "Capers, anchovies, eggplant, capsicum.",
    "Mixed sliced mushrooms and garlic.",
]
pizza_name = [
    "Margherita",
    "Pepperoni",
    "Hawaiian",
    "Neapolitan",
    "Meat Lover's",
    "Margherita con Funghi",
    "BBQ Chicken",
]

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # seeding restaurants
    restaurants = []
    for i in range(10):
        r = Restaurant(
            name=rc(restaurant_name),
            address = fake.address(),
            )
        restaurants.append(r)

    db.session.add_all(restaurants)
    db.session.commit()

    # seeding pizzas
    pizzas = []
    for i in range(10):
        p = Pizza(
            name=rc(pizza_name),
            ingredient=rc(ingredients),
        )
        pizzas.append(p)

    db.session.add_all(pizzas)
    db.session.commit()

    # Adding pizzas to restaurant
    all_restaurant = Restaurant.query.all()
    all_pizzas = Pizza.query.all()

    for restaurant in all_restaurant:
        for _ in range(rc([1, 2, 3])):
            price = randint(1,30)
            pizza = rc(all_pizzas)
            rp = RestaurantPizza(restaurant_id=restaurant.id, pizza_id=pizza.id, price=price)
            db.session.add(rp)

    db.session.commit()
