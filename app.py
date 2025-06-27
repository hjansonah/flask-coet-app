from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the app! Visit /hello-johann to see the HTML page."

@app.route("/hello-johann")
def hello_johann():
    return render_template("hello johann.html")

if __name__ == "__main__":
    app.run(debug=True)
