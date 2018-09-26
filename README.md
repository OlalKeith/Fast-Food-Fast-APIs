[![Build Status](https://travis-ci.com/OlalKeith/ch-API-160779636.svg?branch=ch-API-160779636 )](https://travis-ci.com/OlalKeith/API) 
[![Maintainability](https://api.codeclimate.com/v1/badges/e92621d19014869658e5/maintainability)](https://codeclimate.com/github/OlalKeith/Fast-Food-Fast-APIs/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e92621d19014869658e5/test_coverage)](https://codeclimate.com/github/OlalKeith/Fast-Food-Fast-APIs/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/OlalKeith/Fast-Food-Fast-APIs/badge.svg?branch=ch-API-160779636 )](https://coveralls.io/github/OlalKeith/Fast-Food-Fast-APIs?branch=ch-API-160779636 )

# Fast-Food-Fast-APIs

Fast-Food-Fast is a food delivery service app for a restaurant.


## Features

*Users can fetch orders

*Users can fetch a specific order

*Users can Update there order

*Users can place orders

*Users can delete an order


### Getting started?

*Step 1*

Clone the repo
```git clone repo ```

```cd Fast-Food-Fast-ApIs ```

Create and activate virtual environmnet

```virtualenv venv --distribute ```

```source venv/bin/activate```

Install project dependencies

```pip install flask-restful```

```pip freeze > requirements.txt```

```pip install -r requirements.txt```

*Step 2*

#### Running the application locally
s
```python run.py```

*Step 3*

#### Running the Tests

On the terminal, run ```pytest -v```

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ce5fa5121eb851f81114)

### Orders API-Endpoints

| Url EndPoint           | HTTP Request| Functionality                  	       		   | 
| ---------------------  |-------------|--------------------------------------     		   |
| /orders           	 | GET		   | Get all the orders.            		   		   |
| /orders/<int:order_id> | GET		   | Fetch a specific order using a specific id        |
| /orders          		 | POST 	   | Place a new order.             	       		   |
| /orders/<int:order_id> | PUT		   | Update the status of an order using a specific id.|
| /orders/<int:order_id> | DELETE 	   | Delete the order using a specific id 			   |


# Live Application

This API is hosted on [heroku](https://www.heroku.com/) 

- [Get a list of orders](https://olal-fast-food-api.herokuapp.com/api/v1/orders)
- [Fetch a specific order](https://olal-fast-food-api.herokuapp.com/api/v1/orders/2)


## Licence
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

[w3schools](https://www.w3schools.com/)
