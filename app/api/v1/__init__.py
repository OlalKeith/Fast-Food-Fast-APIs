from flask import Flask 
from flask_restful import Api

import config


def create_app(config_name):


	app = Flask(__name__)
	api  = Api(app)

	app.config.from_object('config')
	app.url_map.strict_slashes = False

	from app.api.v1.fetchOrders import GetOrders
	from app.api.v1.views_orders import GetSingleOrder

	api.add_resource(GetOrders, '/api/v1/orders')
	api.add_resource(GetSingleOrder, '/api/v1/orders/<int:order_id>')

	return app