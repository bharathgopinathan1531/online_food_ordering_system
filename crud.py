from fastapi import HTTPException
from sqlalchemy.orm import Session
import models

def get_restaurants(db):
    return db.query(models.Restaurant).all()

def create_restaurant(db: Session, restaurant):
    db_restaurant = models.Restaurant(
        name=restaurant.name,
        address=restaurant.address,
        phone=restaurant.phone
    )

    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)

    return db_restaurant

def create_food_item(db, food_item):
    db_food = models.FoodItem(
        name=food_item.name,
        price=food_item.price,
        restaurant_id=food_item.restaurant_id
    )

    db.add(db_food)
    db.commit()
    db.refresh(db_food)

    return db_food


def get_food_items(db):
    return db.query(models.FoodItem).filter(models.FoodItem.is_deleted ==False).all()

def create_customer(db, customer):
    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


def get_customers(db):
    return db.query(models.Customer).all()

def create_order(db, order):
    
    customer = db.query(models.Customer).filter(
        models.Customer.id == order.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    food_item = db.query(models.FoodItem).filter(
        models.FoodItem.id == order.food_item_id
    ).first()

    if not food_item:
        raise HTTPException(
            status_code=404,
            detail="Food item not found"
        )

    total = food_item.price * order.quantity

    db_order = models.Order(
        customer_id=order.customer_id,
        food_item_id=order.food_item_id,
        quantity=order.quantity,
        total_amount=total,
        status="Pending"
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order

def get_orders(db):
    return db.query(models.Order).all()


def cancel_order(db, order_id):
    order = db.query(models.Order).filter(
        models.Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.status = "Cancelled"

    db.commit()
    db.refresh(order)

    return order

def update_order_status(db, order_id, status):
    order = db.query(models.Order).filter(
        models.Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if order.status == "Cancelled":
        raise HTTPException(
            status_code=400,
            detail="Cancelled orders cannot be modified"
        )

    order.status = status

    db.commit()
    db.refresh(order)

    return order

# Update Restaurant
def update_restaurant(db, restaurant_id, restaurant):
    db_restaurant = db.query(models.Restaurant).filter(
        models.Restaurant.id == restaurant_id
    ).first()

    if db_restaurant:
        db_restaurant.name = restaurant.name
        db_restaurant.address = restaurant.address
        db_restaurant.phone = restaurant.phone
        db.commit()
        db.refresh(db_restaurant)

    return db_restaurant


# Delete Restaurant
def delete_restaurant(db, restaurant_id):
    db_restaurant = db.query(models.Restaurant).filter(
        models.Restaurant.id == restaurant_id
    ).first()

    if db_restaurant:
        db.delete(db_restaurant)
        db.commit()

    return db_restaurant


# Update Food Item
def update_food_item(db, food_id, food):
    db_food = db.query(models.FoodItem).filter(
        models.FoodItem.id == food_id
    ).first()

    if db_food:
        db_food.name = food.name
        db_food.price = food.price
        db_food.restaurant_id = food.restaurant_id
        db.commit()
        db.refresh(db_food)

    return db_food


# Delete Food Item
def delete_food_item(db, food_id):
    db_food = db.query(models.FoodItem).filter(
        models.FoodItem.id == food_id
    ).first()

    if db_food:
        db_food.is_deleted = True
        db.commit()
        db.refresh(db_food)

    return db_food