from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str
    address: str
    phone: str

class RestaurantResponse(RestaurantCreate):
    id: int

    class Config:
        from_attributes = True
        
class FoodItemCreate(BaseModel):
    name: str
    price: float
    restaurant_id: int        
    
class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str 
    
class OrderCreate(BaseModel):
    customer_id: int
    food_item_id: int
    quantity: int 
    
class LoginSchema(BaseModel):
    username: str
    password: str          