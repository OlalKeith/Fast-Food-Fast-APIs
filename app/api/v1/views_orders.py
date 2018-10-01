from flask import Flask, jsonify, abort, make_response, request 
from flask_restful import Resource, Api
from flask.views import MethodView

from app.api.model import orders

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


class GetAllOrders(MethodView):
    '''Gets orders'''
    def get(self):

        return {'orders': orders}


class GetSingleOrder(MethodView):
    """docstring for GetSpecificOrder"""
    def get(self, order_id):
        order = [order for order in orders if order['order_id'] == order_id]

        return {'orders': order[0]}, 200 if order else 404

class PlaceOrder(MethodView):
    """docstring for placing order"""
    def post(self):
        """requesting the data. If the data isn't there, or if it is there,"""
        """but we are missing a name item then we return an error code 400.bad request"""
        if not request.json or not 'name' in request.json:
            abort(400)
        '''Passed items'''
        price = request.json['price']
        name = request.json['name']

        order = {
         'order_id': len(orders) + 1,
         'price':price,
         'name': name,
         'type': request.json.get('type', "")
        }

        orders.append(order)

        return {'data': orders}, 201
		

class UpdateOrder(MethodView):
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


class DeleteOrder(MethodView):
    """docstring for DeleteOrder"""
    def delete(self,order_id):
        order = [order for order in orders if order['order_id'] == order_id]
        if len(order) == 0:
            abort(404)
        orders.remove(order[0])
        return {'result':True}

delete_meal_view  = DeleteOrder.as_view('delete_meal_view')
update_meal_view = UpdateOrder.as_view('update_meal_view ')
place_order_view = PlaceOrder.as_view('place_order_view')
get_single_order_view = GetSingleOrder.as_view('get_single_order_view')
get_all_orders_view = GetAllOrders.as_view('get_all_orders_view')




