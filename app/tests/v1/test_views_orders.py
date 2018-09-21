import unittest
import json
from app import create_app

class TestGettingAllorders(unittest.TestCase):

	def setUp(self):
		self.app = create_app('test')
		self.app.testing = True
		self.client = self.app.test_client()

	"""Test get all orders"""
	def test_get_orders(self):
		make_response = self.client.get('/api/v1/orders', content_type='application/json')
		self.assertEqual(make_response.status_code, 200)

	"""Test get single orders"""
	def test_single_order(self):
		make_response = self.client.get('/api/v1/orders/<int:order_id>', content_type='application/json')
		self.assertEqual(make_response.status_code, 404)

	def test_place_oder(self):
		make_response = self.client.post('/api/v1/order', content_type='application/json' )
		self.assertEqual(make_response.status_code, 400)