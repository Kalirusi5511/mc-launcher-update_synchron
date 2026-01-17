from flask import Flask, jsonify, send_file, render_template_string
import os

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "status": "ok",
        "service": "mc-launcher-update",
        "endpoints": ["/update"]
    })
    
# =========================
# KONFIGURATION
# =========================
CURRENT_VERSION = "1.1"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPDATE_ZIP = os.path.join(BASE_DIR, "update.zip")

# =========================
# HTML SEITE (STARTSEITE)
# =========================
HTML_PAGE = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>MC Launcher Update</title>
    <style>
        body {
            background-color: #0f172a;
            color: #e5e7eb;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .box {
            text-align: center;
            padding: 40px;
            border-radius: 12px;
            background-color: #020617;
            box-shadow: 0 0 20px rgba(0,255,255,0.3);
        }
        h1 {
            color: #38bdf8;
        }
        .loader {
            margin: 25px auto;
            border: 6px solid #1e293b;
            border-top: 6px solid #38bdf8;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .version {
            margin-top: 15px;
            color: #94a3b8;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>🔄 Update wird ausgeführt</h1>
        <div class="loader"></div>
        <p>Firmware / Custom Initialisierungs-Update läuft…</p>
        <p>Bitte Launcher nicht schließen.</p>
        <div class="version">Aktuelle Server-Version: {{ version }}</div>
    </div>
</body>
</html>
"""

# =========================
# ROUTES
# =========================

@app.route("/")
def index():
    return render_template_string(HTML_PAGE, version=CURRENT_VERSION)

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

# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
