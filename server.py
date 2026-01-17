from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

# === VERSION ===
CURRENT_VERSION = "1"

# === PFAD ZUR update.zip ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPDATE_ZIP = os.path.join(BASE_DIR, "update.zip")

@app.route("/version")
def version():
    return jsonify({"version": CURRENT_VERSION})

@app.route("/update")
def update():
    if not os.path.exists(UPDATE_ZIP):
        return "update.zip nicht gefunden", 404

    return send_file(
        UPDATE_ZIP,
        as_attachment=True,
        download_name="update.zip",
        mimetype="application/zip"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
