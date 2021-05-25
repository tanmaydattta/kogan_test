from flask import Flask, jsonify
from flask_cors import cross_origin
from core import calculate_weight

app = Flask(__name__)


@app.route('/')
@cross_origin()
def index():
    return get_average_weight_for("Air Conditioners")
def get_average_weight_for(category):
    average_weight = calculate_weight(category)
    return jsonify({f'averageWeight for {category}': f"{average_weight} kg"})

@app.route('/<category>')
@cross_origin()
def on_demand(category):
    return get_average_weight_for(category)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)