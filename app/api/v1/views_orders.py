from flask import Flask, jsonify, abort, make_response
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

        api.add_resource(GetAllOrders, '/api/v1/orders')
