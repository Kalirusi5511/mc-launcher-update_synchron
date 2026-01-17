from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

CURRENT_VERSION = "1.1"

@app.route("/version")
def version():
    return jsonify({"version": CURRENT_VERSION})

@app.route("/update")
def update():
    file_path = os.path.join(os.getcwd(), "update.zip")
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.
