from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)


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


# @app.route('/api/v1/orders/', methods=['GET'])
# def get_orders():
#     return jsonify({'orders': orders})


@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # global order
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'orders': order[0]})


if __name__ == '__main__':
    app.run(debug=True)
