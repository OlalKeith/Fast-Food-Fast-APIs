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


if __name__ == '__main__':
    app.run(debug=True)
