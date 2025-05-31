from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="bouncym2025",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()

# Load all records once (you can optimize this later with pagination)
cur.execute('SELECT "Coet ID", "Coet", "Still valid", "Source", "date coet" FROM "Coets Android appended"')
rows = cur.fetchall()

data = [
    {
        "Coet ID": r[0],
        "Coët": r[1],
        "Still valid": r[2],
        "Source": r[3],
        "date coet": r[4]
    } for r in rows
]


@app.route("/")
def index():
    return redirect(url_for('record', index=0))


@app.route("/record/<int:index>")
def record(index):
    if 0 <= index < len(data):
        return render_template("record.html", row=data[index], index=index, total=len(data))
    else:
        return "Index out of range", 404


@app.route("/update", methods=["POST"])
def update():
    index = int(request.form["index"])
    value = request.form["value"] == "True"
    coet_id = data[index]["Coet ID"]

    cur.execute('UPDATE "Coets Android appended" SET "Still valid" = %s WHERE "Coet ID" = %s', (value, coet_id))
    conn.commit()

    # Update the local data list too
    data[index]["Still valid"] = value

    return jsonify(success=True)


@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

