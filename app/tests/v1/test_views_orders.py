import unittest, os , sys
from app.api.model import orders
from flask.views import MethodView
import json


from app import create_app

class OrderTestCase(unittest.TestCase):

	def setUp(self):
		self.app = create_app("testing")
		self.app.testing = True
		self.client = self.app.test_client()
		self.data = {
					"order_id": 2,
					"name": "beef roast",
					"price": "Ksh800",
					"type": "Meat"
					}

	"""Test get all orders"""
	def test_get_orders(self):
	 	make_response = self.client.get('/api/v1/orders', content_type='application/json')
	 	self.assertEqual(make_response.status_code, 200)

	"""Test get single orders"""
	def test_single_order(self):
		make_response = self.client.get('/api/v1/order/1', content_type='application/json')
		result = json.loads(make_response.data)
		print (result)
		self.assertEqual(make_response.status_code, 200)


	"""Test update orders"""
	def test_update_order(self):
		make_response = self.client.put('/api/v1/order/1', content_type = 'application/json')
		self.assertEqual(make_response.status_code, 200)
		self.assertNotEqual(make_response.status_code, 404)
		"""Test place orders"""
	def test_place_order(self):
		make_response = self.client.post('/api/v1/orders', content_type='application/json' )
		# result = json.loads(make_response.data)
		self.assertEqual(make_response.status_code, 201)
		# self.assertEqual(result["message"], "order added")

	# 	"""Test delete an order"""
	# def test_delete_oder(self):
	# 	make_response = self.client.post('/api/v1/orders/<int:order_id>', content_type='application/json' )
	# 	self.assertEqual(make_response.status_code, 404)


