from flask import Flask 
from flask_restful import Api

import config


def create_app(config_name):


	app = Flask(__name__, instance_relative_config=True)
	api  = Api(app)

	app.config.from_object('config')
	app.url_map.strict_slashes = False

	from app.api.v1.views_orders import GetAllOrders
	from app.api.v1.views_orders import GetSingleOrder
	from app.api.v1.views_orders import UpdateOrder

	api.add_resource(GetAllOrders, '/api/v1/orders')
	api.add_resource(GetSingleOrder, '/api/v1/orders/<int:order_id>')
	api.add_resource(UpdateOrder, '/api/v1/orders/<int:order_id>')

	return app