import json

from flask import Flask, render_template

app = Flask(__name__)


def datab(src_file='product_db.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/products')
def products():
    info = datab()
    return render_template('products.html', products=info)


@app.route('/product/<prod_id>')
def details(prod_id):
    info = datab()
    return render_template('product_details.html', products=info, prod_id=prod_id)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
