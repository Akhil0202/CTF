from flask import request
import sqlite3

@app.route("/login")
def login():
    username = request.args.get("u")
    query = "SELECT * FROM users WHERE name='" + username + "'"
    cursor.execute(query)
