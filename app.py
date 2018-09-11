from flask import Flask, jsonify, abort, make_response,  request
import os

app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

orders = [

   {
        'id': 1,
        'quantity': '1',
        'name': 'beef roast',
        'type': 'Meat',
        
    },

    {
        'id': 2,
        'quantity': '1 package',
        'name': 'dried Italian salad dressing mix',
        'type': 'Condiments',
        
    },

       {
        'id': 3,
        'quantity': '1',
        'name': 'water',
        'type': 'drinks',
        
    }

]


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})


@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def fetch_order(order_id):
    # global order
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'orders': order[0]})


@app.route('/api/v1/orders', methods=['POST'])
def place_order():
      
    if not request.json or not 'name' in request.json:
        abort(400)

    order = {
        'id': orders[-1]['id'] + 1,
        'quantity':request.json['quantity'],
        'name': request.json['name'],
        'type': request.json.get('type', ""),



    }
    orders.append(order)
    return jsonify({'order': order}), 201


@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    # global order
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'type' in request.json and type(request.json['type']) != unicode:
        abort(400)
    if 'quantity' in request.json and type(request.json['quantity']) != unicode:
        abort(400)
    order[0]['name'] = request.json.get('name', order[0]['name'])
    order[0]['type'] = request.json.get('type', order[0]['type'])
    order[0]['quantity'] = request.json.get('quantity', order[0]['quantity'])
            
    return jsonify({'order': order[0]})

    order = {
        'id': orders[-1]['id'] + 1,
        'quantity':request.json['quantity'],
        'name': request.json['name'],
        'type': request.json.get('type', ""),



    }
# if __name__ == '__main__':
#     # app.run(debug=True)
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host ='0.0.0.0', port=port)
