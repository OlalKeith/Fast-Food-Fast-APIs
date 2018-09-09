from flask import Flask, jsonify, abort, make_response, request


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


if __name__ == '__main__':
    app.run(debug=True)
