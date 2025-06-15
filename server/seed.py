from server.app import db, create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

def seed_data():
    with app.app_context():
        db.session.query(RestaurantPizza).delete()
        db.session.query(Restaurant).delete()
        db.session.query(Pizza).delete()
        
        r1 = Restaurant(name="Pizza Palace", address="123 Main St")
        r2 = Restaurant(name="Italian Bistro", address="456 Oak Ave")
        r3 = Restaurant(name="Slice of Heaven", address="789 Pine Rd")
        
        p1 = Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil")
        p2 = Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni")
        p3 = Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms, onions")
        
        db.session.add_all([r1, r2, r3, p1, p2, p3])
        db.session.commit()
        
        rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
        rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
        rp3 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p3.id)
        rp4 = RestaurantPizza(price=8, restaurant_id=r3.id, pizza_id=p1.id)
        
        db.session.add_all([rp1, rp2, rp3, rp4])
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()