import os
import psycopg2

def connect_db(config=None):
	'''connect database'''
	if config == 'testing':
		db_name = os.getenv('test_fast_food')
	else:
		db_name = os.getenv('fast_food_fast')

		user = os.getenv('username')
		password = os.getenv('password')
		host = os.getenv('host')
		port = os.getenv('port')

		return psycopg2.connect(user=user, password=password, host=host, port=port, database=db_name)

def table_order(cur):

	cur.execute(
		'''CREATE TABLE users(
		id serial PRIMARY KEY,
		username VACHAR NOT NULL UNIQUE,
		email VARCHAR NOT NULL UNIQUE,
		password VARCHAR NOT NULL);''')


	cur = connection.cursor()
	# cur.executea
	table_order(cur)
	connection.commit()
	cur.close()
	connection.close()

	print('created') 





if __name__ == '__main__':
	app.run(debug = True)