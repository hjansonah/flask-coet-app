import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the app! Visit /hello-johann to see the HTML page."

@app.route("/hello-johann")
def hellojohann():
    return render_template("hellojohann.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT env var (Render sets this)
    app.run(host="0.0.0.0", port=port)
