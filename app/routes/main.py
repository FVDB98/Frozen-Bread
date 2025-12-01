from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/menu")
def menu():
    return render_template("menu.html")

@main.route("/pricing")
def pricing():
    return render_template("pricing.html")

@main.route("/faq")
def faq():
    return render_template("faq.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")
