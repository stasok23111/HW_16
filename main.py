
from flask_sqlalchemy import SQLAlchemy
from models import User, Offer, Order
from flask import jsonify, Flask, request, abort
from utils import data_db
from init_db import db
from config import Config

app = Flask(__name__)


@app.route('/users/', methods=['GET', 'POST'],)
def get_users():
    if request.method == 'GET':

        try:
            users = db.session.query(User).all()
            return jsonify([user.serialize() for user in users])
        except Exception as e:
            return f'{e}]'
    elif request.method == 'POST':
        data = request.json
        db.session.add(User(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'],)
def get_user(user_id):
    if request.method == 'GET':
        try:
            user = db.session.query(User).filter(User.id == user_id).first()
            return jsonify(user.serialize())
        except Exception as e:
            return f'{e}'
    elif request.method == 'PUT':
        user = db.session.query(User).filter(User.id == user_id).first()
        if user is None:
            abort(404)
        db.session.query(User).filter(User.id == user_id).update(request.json)
        db.session.commit()
        return jsonify(code=200)
    elif request.method == 'DELETE':
        count = db.session.query(User).filter(User.id == user_id).delete()
        db.session.commit()
        if not count:
            aort(404)
        return jsonify(code=200)


@app.route('/orders/', methods=['GET', 'POST'],)
def get_orders():
    if request.method == 'GET':
        try:
            orders = db.session.query(Order).all()
            return jsonify([order.serialize() for order in orders])
        except Exception as e:
            return f'{e}]'
    elif request.method == 'POST':
        data = request.json
        db.session.add(Order(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'],)
def get_order(order_id):
    if request.method == 'GET':

        try:
            order = db.session.query(Order).filter(Order.id == order_id).first()
            return jsonify(order.serialize())
        except Exception as e:
            return f'{e}'
    elif request.method == 'PUT':
        order = db.session.query(Order).filter(Order.id == order_id).first()
        if order is None:
            abort(404)
        db.session.query(Order).filter(Order.id == order_id).update(request.json)
        db.session.commit()
    elif request.method == 'DELETE':
        count = db.session.query(Order).filter(Order.id == order_id).delete()
        db.session.commit()
        if not count:
            aort(404)
        return jsonify(code=200)


@app.route('/offers/', methods=['GET', 'POST'],)
def get_offers():
    if request.method == 'GET':
        try:
            offers = db.session.query(Offer).all()
            return jsonify([offer.serialize() for offer in offers])
        except Exception as e:
            return f'{e}]'
    elif request.method == 'POST':
        data = request.json
        db.session.add(Offer(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'],)
def get_offer(offer_id):
    if request.method == 'GET':
        try:
            offer = db.session.query(Offer).filter(Offer.id == offer_id).first()
            return jsonify(offer.serialize())
        except Exception as e:
            return f'{e}'
    elif request.method == 'PUT':
        offer = db.session.query(Offer).filter(Offer.id == offer_id).first()
        if offer is None:
            abort(404)
        db.session.query(Offer).filter(Offer.id == offer_id).update(request.json)
        db.session.commit()
    elif request.method == 'DELETE':
        count = db.session.query(Offer).filter(Offer.id == offer_id).delete()
        db.session.commit()
        if not count:
            aort(404)
        return jsonify(code=200)


if __name__ == '__main__':

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        data_db()

    app.run(debug=True)
