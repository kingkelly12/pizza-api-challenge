from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

def seed_data():
    db.drop_all()
    db.create_all()

    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Cheesy Bites", address="456 Elm St"),
        Restaurant(name="Kiki's Pizza", address="789 Oak St"),
        Restaurant(name="Slice of Heaven", address="101 Maple Ave"),
        Restaurant(name="Mario's Pizzeria", address="202 Pine St")
    ]
    db.session.add_all(restaurants)
    db.session.commit()

    pizzas = [
        Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni"),
        Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Mushrooms, Onions"),
        Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Mozzarella, Ham, Pineapple"),
        Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Mozzarella, Chicken, Red Onions"),
        Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    ]
    db.session.add_all(pizzas)
    db.session.commit()

    restaurant_pizzas = [
        RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
        RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
        RestaurantPizza(price=15, pizza_id=3, restaurant_id=2),
        RestaurantPizza(price=11, pizza_id=4, restaurant_id=2),
        RestaurantPizza(price=13, pizza_id=5, restaurant_id=3),
        RestaurantPizza(price=9, pizza_id=6, restaurant_id=3),
        RestaurantPizza(price=14, pizza_id=1, restaurant_id=4),
        RestaurantPizza(price=8, pizza_id=2, restaurant_id=4),
        RestaurantPizza(price=16, pizza_id=3, restaurant_id=5),
        RestaurantPizza(price=18, pizza_id=4, restaurant_id=5),
        RestaurantPizza(price=5, pizza_id=1, restaurant_id=3)  
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_data()