from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud
import auth
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/restaurants")
def create_restaurant(
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    return crud.create_restaurant(db, restaurant)

@app.get("/restaurants")
def get_restaurants(
    db: Session = Depends(get_db)
):
    return crud.get_restaurants(db)

@app.post("/food-items")
def create_food_item(
    food_item: schemas.FoodItemCreate,
    db: Session = Depends(get_db)
):
    return crud.create_food_item(db, food_item)


@app.get("/food-items")
def get_food_items(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return db.query(models.FoodItem).offset(skip).limit(limit).all()

@app.post("/customers")
def create_customer(
    customer: schemas.CustomerCreate,
    db: Session = Depends(get_db)
):
    return crud.create_customer(db, customer)


@app.get("/customers")
def get_customers(
    db: Session = Depends(get_db)
):
    return crud.get_customers(db)


@app.post("/orders")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order(db, order)

@app.get("/orders")
def get_orders(
    db: Session = Depends(get_db)
):
    return crud.get_orders(db)

@app.put("/orders/{order_id}/cancel")
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    return crud.cancel_order(db, order_id)

@app.put("/orders/{order_id}/status")
def update_order_status(
    order_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    return crud.update_order_status(
        db,
        order_id,
        status
    )
    
@app.put("/restaurants/{restaurant_id}")
def update_restaurant(
    restaurant_id: int,
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    return crud.update_restaurant(db, restaurant_id, restaurant)


@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_restaurant(db, restaurant_id)

@app.put("/food-items/{food_id}")
def update_food_item(
    food_id: int,
    food: schemas.FoodItemCreate,
    db: Session = Depends(get_db)
):
    return crud.update_food_item(db, food_id, food)


@app.delete("/food-items/{food_id}")
def delete_food_item(
    food_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_food_item(db, food_id)

@app.get("/food-items/search")
def search_food_items(
    name: str,
    db: Session = Depends(get_db)
):
    return db.query(models.FoodItem).filter(
        models.FoodItem.name.contains(name)
    ).all()
    
@app.post("/login")
def login(user: schemas.LoginSchema):

    if user.username == "admin" and user.password == "admin123":
        token = auth.create_access_token(
            {"sub": user.username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    return {"message": "Invalid credentials"}    