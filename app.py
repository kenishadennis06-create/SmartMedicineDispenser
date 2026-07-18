from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Smart Medicine Dispenser</h1><p>Flask is working!</p>"

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
