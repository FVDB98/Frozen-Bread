from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.database import get_db
from app.models import User

auth = Blueprint("auth", __name__)


# -----------------------------
# LOGIN PAGE (GET)
# -----------------------------
@auth.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


# -----------------------------
# LOGIN LOGIC (POST)
# -----------------------------
@auth.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    db = get_db()

    row = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

    if row is None:
        flash("No account with that email.", "error")
        return redirect(url_for("auth.login_page"))


    user = User(
        row["id"],
        row["name"],
        row["email"],
        row["password_hash"],
        row["address_line1"],
        row["address_line2"],
        row["city"],
        row["postcode"],
        row["country"],
        row["created_at"],
        row["is_admin"]
    )

    if not check_password_hash(user.password_hash, password):
        flash("Incorrect password.", "error")
        return redirect(url_for("auth.login_page"))

    login_user(user)
    return redirect(url_for("account.account_home"))
    


# -----------------------------
# REGISTER PAGE (GET)
# -----------------------------
@auth.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


# -----------------------------
# REGISTER LOGIC (POST)
# -----------------------------
@auth.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    address_line1 = request.form.get("address_line1")
    address_line2 = request.form.get("address_line2")
    city = request.form.get("city")
    postcode = request.form.get("postcode")
    country = request.form.get("country")

    if not name or not email or not password or not address_line1 or not postcode or not country:
        flash("Please fill all required fields.", "error")
        return redirect(url_for("auth.register_page"))

    db = get_db()

    # Check for existing email
    existing = db.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()

    if existing:
        flash("An account with this email already exists.", "error")
        return redirect(url_for("auth.register_page"))

    password_hash = generate_password_hash(password)

    db.execute("""
        INSERT INTO users (
            name, email, password_hash,
            address_line1, address_line2, city,
            postcode, country
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, email, password_hash,
        address_line1, address_line2, city,
        postcode, country
    ))

    db.commit()

    # Log the user in
    new_user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

    user = User(
        new_user["id"], new_user["name"], new_user["email"], new_user["password_hash"],
        new_user["address_line1"], new_user["address_line2"], new_user["city"],
        new_user["postcode"], new_user["country"], new_user["created_at"], new_user["is_admin"]
    )

    login_user(user)
    return redirect(url_for("account.account_home"))

# -----------------------------
# USER LOGOUT
# -----------------------------
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
