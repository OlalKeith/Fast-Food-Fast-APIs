from flask import Flask, jsonify, abort, make_response, request 
from flask_restful import Resource, Api, reqparse
from flask.views import MethodView

from app.api.model import orders

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('name', type=str,help='enter a name for the order',required=True, location='json')
parser.add_argument('type', type=str, location='json')
parser.add_argument('price', type=int,help='price can\'t be empty', required=True, location='json')

class GetAllOrders(MethodView):
    '''Gets orders'''
    def get(self):

        data =  jsonify(orders)
        data.status_code = 200
        return data
       


class GetSingleOrder(MethodView):
    """docstring for GetSpecificOrder"""
    def get(self, order_id): 
        order = [order for order in orders if order['order_id'] == order_id]
        if len(order) == 0:
            return jsonify({'Error': 'Order not found'}), 404
        data = jsonify(order)
        return data, 200

        


class PlaceOrder(MethodView):
    """Endpoint for POST requests. Creates a new order."""
    def post(self):
        '''Passed items'''

        args = parser.parse_args()
        order = [order for order in orders if order['name'] == args['name'] ]
        #  remove all the leading and trailing spaces
        if args['name'].strip() == "":
            return jsonify({'Error':'Order must have a valid name'}), 400

        order = {
         'order_id': len(orders) + 1,
         'price':args['price'],
         'name': args['name'],
         'type': args['type']
        }
        # add each 'order' to my 'orders'
        orders.append(order)
        # status code = created
        data = {'order': order}
        return jsonify(data), 201

		

class UpdateOrder(MethodView):
    """Endpoint for PUT requests. Edits a specific order"""
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


# class DeleteOrder(MethodView):
#     """docstring for DeleteOrder"""
#     def delete(self,order_id):
#         order = [order for order in orders if order['order_id'] == order_id]
#         if len(order) == 0:
#             abort(404)
#         orders.remove(order[0])
#         return {'result':True}

# delete_meal_view  = DeleteOrder.as_view('delete_meal_view')
update_meal_view = UpdateOrder.as_view('update_meal_view ')
place_order_view = PlaceOrder.as_view('place_order_view')
get_single_order_view = GetSingleOrder.as_view('get_single_order_view')
get_all_orders_view = GetAllOrders.as_view('get_all_orders_view')

# api.add_resource(GetSingleOrder, '/api/v1/order/<int:order_id>')




