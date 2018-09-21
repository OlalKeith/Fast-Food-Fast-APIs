from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource, Api

from app.api.model import orders

app = Flask(__name__)
api = Api(app)

# orders = []
# id = 0

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


class GetAllOrders(Resource):
    '''Gets orders'''
    def get(self):

        return {'orders': orders}


class GetSingleOrder(Resource):
    """docstring for GetSpecificOrder"""
    def get(self, order_id):
        order = [order for order in orders if order['order_id'] == order_id]

        return {'orders': order[0]}, 200 if order else 404

class PlaceOrder(Resource):
    """docstring for placing order"""
    def post(self):
        """requesting the data. If the data isn't there, or if it is there,"""
        """but we are missing a name item then we return an error code 400.bad request"""
        if not request.json or not 'name' in request.json:
            abort(400)

        order = {
            'order_id': orders[-1]['order_id'] + 1,
            'price':request.json['price'],
            'name': request.json['name'],
            'type': request.json.get('type', ""),
        }
        orders.append(order)
        return {'order': order}, 201

        



		


