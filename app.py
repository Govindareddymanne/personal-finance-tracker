from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "finance_secret_key"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Govind@123",
    database="finance_db"
)
cursor = db.cursor(dictionary=True)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
            (name, email, password)
        )
        db.commit()
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    cursor.execute(
        "SELECT * FROM transactions WHERE user_id=%s ORDER BY created_at DESC",
        (user_id,)
    )
    transactions = cursor.fetchall()

    cursor.execute(
        "SELECT SUM(CASE WHEN type='income' THEN amount ELSE -amount END) AS balance "
        "FROM transactions WHERE user_id=%s",
        (user_id,)
    )
    balance = cursor.fetchone()["balance"] or 0

    return render_template(
        "dashboard.html",
        transactions=transactions,
        balance=balance
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        type_ = request.form["type"]

        cursor.execute(
            "INSERT INTO transactions (user_id, amount, category, type) "
            "VALUES (%s,%s,%s,%s)",
            (session["user_id"], amount, category, type_)
        )
        db.commit()
        return redirect(url_for("dashboard"))

    return render_template("add_expense.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


