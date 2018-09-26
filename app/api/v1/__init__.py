import os
from flask import Flask 
from flask_restful import Api

# LOCALPATH = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, LOCALPATH + '/../../../')

from instance.config import app_config


def create_app(config_name = 'testing'):


	app = Flask(__name__, instance_relative_config=True)
	api  = Api(app)

	# app.config.from_object('instance.config')
	app.config.from_object(app_config["testing"])
	app.config.from_pyfile('config.py')
	app.url_map.strict_slashes = False

	from app.api.v1.views_orders import GetAllOrders
	from app.api.v1.views_orders import GetSingleOrder
	from app.api.v1.views_orders import UpdateOrder
	from app.api.v1.views_orders import DeleteOrder
	from app.api.v1.views_orders import PlaceOrder

	api.add_resource(GetAllOrders, '/api/v1/orders')
	api.add_resource(GetSingleOrder, '/api/v1/orders/<int:order_id>')
	api.add_resource(UpdateOrder, '/api/v1/orders/<int:order_id>')
	api.add_resource(DeleteOrder, '/api/v1/orders/<int:order_id>')
	api.add_resource(PlaceOrder, '/api/v1/order')

	return app