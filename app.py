import requests
from flask import Response, request

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

@app.route("/image")
def proxy_image():
    img_url = request.args.get("url")
    if not img_url:
        return "Missing URL", 400
    r = requests.get(img_url, stream=True)
    return Response(r.content, content_type=r.headers['Content-Type'])
