from flask import Flask, jsonify
from flask_cors import cross_origin

HOST = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
ENDPOINT = '/api/products/1'

app = Flask(__name__)


@app.route('/')
@cross_origin()
def index():
    average_weight = 10
    return jsonify({f'averageWeight': "{average_weight} kg"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)