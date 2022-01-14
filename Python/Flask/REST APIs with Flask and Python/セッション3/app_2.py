from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

products = [
    {'id': 1, 'name':'商品1', 'price':780},
    {'id': 2, 'name':'商品2', 'price':1280},
    {'id': 3, 'name':'商品3', 'price':1980},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def get_products():
    return jsonify({'products': products})


@app.route('/product', methods=['POST'])
def create_product():
    new_product = {'id': products[-1]['id']+1}
    post_data = request.get_json()
    new_product.update(list(post_data.items()))

    print('request_data')
    print(new_product)

    products.append(new_product)

    return jsonify({'products': products})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')