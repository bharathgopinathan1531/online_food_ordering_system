Online Food Ordering System

Objective

A backend application built using FastAPI, SQLAlchemy, Pydantic, and SQLite to manage restaurants, food items, customers, and orders.

Features

Restaurant Management

- Add Restaurant
- View Restaurants

Food Item Management

- Add Food Item
- View Food Items

Customer Management

- Add Customer
- View Customers

Order Management

- Place Order
- View Orders
- Cancel Order
- Update Order Status

Business Rules

- Customer must exist before placing an order.
- Food item must exist before placing an order.
- Order total is calculated automatically.
- Cancelled orders cannot be modified.

Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

Installation

pip install -r requirements.txt

Run Application

uvicorn main:app --reload

Swagger Documentation

Open in browser:

http://127.0.0.1:8000/docs

Database Files

- schema.sql
- sql_tasks.sql

Author

Bharath G