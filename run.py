import os

from app import create_app

# config = os.getenv('APP_SETTINGS')
# app = create_app(config)
app = create_app(os.getenv('APP_SETTINGS'))

if __name__ == "__main__":
	app.run(debug=True)





# import os
# from app.api.v1.fetchOrders import app

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)