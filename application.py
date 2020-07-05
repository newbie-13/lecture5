from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    currency = request.form.get("currency")

    res = requests.get("http://data.fixer.io/api/latest", params = {"access_key": "f0520f941d2c2bf56b2ae5fdc69c0cba", "symbols": currency})

    if res.status_code != 200:
        return jsonify({"success": False})

    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})
