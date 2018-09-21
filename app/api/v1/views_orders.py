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

		

class UpdateOrder(Resource):
    """docstring for UpdateOrder"""
    def put(self, order_id):
        order = [order for order in orders if order['order_id'] == order_id]
    # prevent bugs by doing exhaustive checking of the input arguments
        if len(order) == 0:
            abort(404)
        if not request.json:
            abort(400)
        if 'name' in request.json and type(request.json['name']) != unicode:
            abort(400)
        if 'type' in request.json and type(request.json['type']) != unicode:
            abort(400)
        if 'price' in request.json and type(request.json['price']) != unicode:
            abort(400)
        order[0]['name'] = request.json.get('name', order[0]['name'])
        order[0]['type'] = request.json.get('type', order[0]['type'])
        order[0]['price'] = request.json.get('price', order[0]['price'])
            
        return {'order': order[0],'message': 'Updated successfully'}, 200


class DeleteOrder(Resource):
    """docstring for DeleteOrder"""
    def delete(self,order_id):
        order = [order for order in orders if order['order_id'] == order_id]
        if len(order) == 0:
            abort(404)
        orders.remove(order[0])
        return {'result':True}
        

        
