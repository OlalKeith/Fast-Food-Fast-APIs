[![Build Status](https://travis-ci.org/OlalKeith/Fast-Food-Fast-APIs.svg?branch=ch-API-160779636)](https://travis-ci.org/OlalKeith/Fast-Food-Fast-APIs)
[![Maintainability](https://api.codeclimate.com/v1/badges/e92621d19014869658e5/maintainability)](https://codeclimate.com/github/OlalKeith/Fast-Food-Fast-APIs/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e92621d19014869658e5/test_coverage)](https://codeclimate.com/github/OlalKeith/Fast-Food-Fast-APIs/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/OlalKeith/Fast-Food-Fast-APIs/badge.svg?branch=ch-API-160779636 )](https://coveralls.io/github/OlalKeith/Fast-Food-Fast-APIs?branch=ch-API-160779636 )

# Fast-Food-Fast-APIs

Fast-Food-Fast is a food delivery service app for a restaurant.


## Features

* Users can fetch orders

* Users can fetch a specific order

* Users can Update there order

* Users can place orders

* Users can delete an order


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

### Orders API-Endpoints

| Url EndPoint           | HTTP Request| Functionality                  	       		   | 
| ---------------------  |-------------|--------------------------------------     		   |
| /api/v1/orders        | GET		   | Get all the orders.            		   		   |
| /api/v1/orders/<int:order_id> | GET	| Fetch a specific order using a specific id       |
| /api/v1/order          | POST 	   | Place a new order.             	       		   |
| /api/v1/orders/<int:order_id> | PUT	| Update the status of an order using a specific id.|
| /api/v1/orders/<int:order_id>| DELETE | Delete the order using a specific id 			   |


# Live Application 

- [Get a list of orders](https://olal-fast-food-api.herokuapp.com/api/v1/orders)
- [Fetch a specific order](https://olal-fast-food-api.herokuapp.com/api/v1/orders/2)


## Licence
This project is licensed under the MIT License.

## Acknowledgments

[w3schools](https://www.w3schools.com/)

![screenshot from 2018-09-08 18-33-24](https://user-images.githubusercontent.com/13969404/46113094-b3a6c700-c1f5-11e8-9691-46f7a20ebeb6.png)
![screenshot from 2018-09-08 18-47-09](https://user-images.githubusercontent.com/13969404/46113095-b3a6c700-c1f5-11e8-8d83-72b2aa865c06.png)
![screenshot from 2018-09-08 19-20-18](https://user-images.githubusercontent.com/13969404/46113180-02546100-c1f6-11e8-890b-32db83c912c2.png)
