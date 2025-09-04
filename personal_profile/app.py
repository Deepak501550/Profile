from flask import Flask, render_template, send_from_directory, jsonify
import os
import json

app = Flask(__name__, static_folder="static", template_folder="templates")

# Path to data.json
DATA_PATH = os.path.join(os.path.dirname(__file__), "data.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data.json")
def data():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve static files (images, css, js)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
