from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()

@app.route("/login")
def login():
    username = request.args.get("u")
    query = "SELECT * FROM users WHERE name='" + username + "'"
    cursor.execute(query)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
