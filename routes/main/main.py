from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("main/home.html")


@main.route("/about")
def about():
    return render_template("main/about.html")


@main.route("/activities")
def activities():
    return render_template("main/activities.html")


@main.route("/catalog")
def catalog():
    return render_template("main/catalog.html")


@main.route("/contact")
def contact():
    return render_template("main/contact.html")

