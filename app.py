
from flask import Flask, jsonify
import json, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
with open("products.json") as f:
    PRELOADED_PRODUCTS = json.load(f)

@app.route("/products")
def products():
    return jsonify(PRELOADED_PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
