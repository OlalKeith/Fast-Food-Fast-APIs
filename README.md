[![Build Status](https://travis-ci.com/OlalKeith/ch-API-160779636.svg?branch=ch-API-160779636 )](https://travis-ci.com/OlalKeith/API) 
[![Maintainability](https://api.codeclimate.com/v1/badges/e92621d19014869658e5/maintainability)](https://codeclimate.com/github/OlalKeith/Fast-Food-Fast-APIs/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e92621d19014869658e5/test_coverage)](https://codeclimate.com/github/OlalKeith/Fast-Food-Fast-APIs/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/OlalKeith/Fast-Food-Fast-APIs/badge.svg?branch=ch-API-160779636 )](https://coveralls.io/github/OlalKeith/Fast-Food-Fast-APIs?branch=ch-API-160779636 )

# Fast-Food-Fast-APIs

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

#### Running the application

```python run.py```

*Step 3*

#### Testing

On the terminal, run ```pytest -v```

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ce5fa5121eb851f81114)

### API-Endpoints

| EndPoint              | Functionality                  |
| --------------------- | ------------------------------ |
| GET /orders           | Get all the orders.            |
| GET /orders/<orderId> | Fetch a specific order         |
| POST /orders          | Place a new order.             |
| PUT /orders/<orderId> | Update the status of an order. |


# Live Application

This API is hosted on [heroku](https://www.heroku.com/) 

- [Get a list of orders](https://olal-fast-food-api.herokuapp.com/api/v1/orders)
- [Fetch a specific order](https://olal-fast-food-api.herokuapp.com/api/v1/orders/2)