import json

from init_db import db
from models import User, Offer, Order


def insert_data_users(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get('id'),
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                age=row.get('age'),
                email=row.get('email'),
                role=row.get('role'),
                phone=row.get('phone'),

            )
        )
        db.session.commit()


def insert_data_orders(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get('id'),
                name=row.get('name'),
                description=row.get('description'),
                start_date=row.get('start_date'),
                end_date=row.get('end_date'),
                address=row.get('address'),
                price=row.get('price'),
                customer_id=row.get('customer_id'),
                executor_id=row.get('executor_id'),

            )
        )
        db.session.commit()


def insert_data_offers(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get('id'),
                order_id=row.get('order_id'),
                executor_id=row.get('executor_id'),

            )
        )
        db.session.commit()


def data_db():
    with open("data/users.json") as file:
        insert_data_users(json.load(file))

    with open("data/orders.json") as file:
        insert_data_orders(json.load(file))

    with open("data/offers.json") as file:
        insert_data_offers(json.load(file))
