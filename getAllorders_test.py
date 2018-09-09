import unittest
import json
import pytest
from getAllorders import *


# class GetAllorders(unittest.Testcase):
	# """docstring for ClassName"""
def test_get_All_orders():
	result = get_orders.test_client()
	make_response = result.get('/api/v1/orders', content_type = 'application/json')
	assert(make_response.status_code == 200)

		
# if __name__ == '__main__':
# 	unittest.main()