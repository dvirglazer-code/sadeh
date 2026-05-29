from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from sadeh_engine import sadeh_search
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    product = data.get("product", "").strip()
    if not product:
        return jsonify({"error": "Please enter a product name."}), 400
    result = sadeh_search(product)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
