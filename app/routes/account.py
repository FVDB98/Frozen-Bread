from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.database import get_db

account = Blueprint("account", __name__)

@account.route("/account")
@login_required
def account_home():
    return render_template("account.html", user=current_user)

@account.route("/account/address", methods=["GET", "POST"])
@login_required
def update_address():

    db = get_db()

    if request.method == "POST":
        line1 = request.form.get("address_line1")
        line2 = request.form.get("address_line2")
        city = request.form.get("city")
        postcode = request.form.get("postcode")
        country = request.form.get("country")

        # Validate required fields
        if not line1 or not postcode or not country:
            flash("Please complete all required fields.", "error")
            return redirect(url_for("account.update_address"))

        # Update DB
        db.execute("""
            UPDATE users
            SET address_line1 = ?, address_line2 = ?, city = ?, postcode = ?, country = ?
            WHERE id = ?
        """, (line1, line2, city, postcode, country, current_user.id))

        db.commit()

        flash("Address updated successfully.", "success")
        return redirect(url_for("account.account_home"))

    # GET request: show form with existing values
    return render_template("update_address.html", user=current_user)
