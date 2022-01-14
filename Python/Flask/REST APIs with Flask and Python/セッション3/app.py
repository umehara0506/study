from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {'name': 'My Item',
            'price': 15.99}
        ]
    }
]

# POST /store date: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>') # http://127.0.0.1:5000/store/store_name
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_sotre():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name: , price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string:name>/item
@app.route('/store')
def get_item_in_store():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')