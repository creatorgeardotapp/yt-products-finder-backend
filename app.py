
from flask import Flask, jsonify, Response, request
import json, requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load products
with open("products.json") as f:
    PRELOADED_PRODUCTS = json.load(f)

@app.route("/products")
def products():
    return jsonify(PRELOADED_PRODUCTS)

@app.route("/image")
def proxy_image():
    img_url = request.args.get("url")
    if not img_url:
        return "Missing URL", 400
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    }
    r = requests.get(img_url, headers=headers, stream=True)
    return Response(r.content, content_type=r.headers.get('Content-Type', 'image/jpeg'))

@app.route("/status")
def status():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
