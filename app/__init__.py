import os

from flask import Flask 
from flask_restful import Api

from config import app_config


def create_app(config_name= 'testing'):


	app = Flask(__name__, instance_relative_config=True)
	api  = Api(app)

	app.config.from_object(app_config["testing"])
	app.url_map.strict_slashes = False

	from api.v1.views_orders import get_all_orders_view 
	from app.api.v1.views_orders import get_single_order_view
	from app.api.v1.views_orders import update_meal_view
	from app.api.v1.views_orders import delete_meal_view
	from app.api.v1.views_orders import place_order_view

	app.add_url_rule('/api/v1/orders' , view_func = get_all_orders_view)
	app.add_url_rule('/api/v1/orders/<int:order_id>' , view_func = update_meal_view)
	app.add_url_rule('/api/v1/orders/<int:order_id>' , view_func = get_single_order_view)
	app.add_url_rule('/api/v1/order' , view_func = place_order_view)
	app.add_url_rule('/api/v1/orders/<int:order_id>' , view_func = delete_meal_view)


	return app