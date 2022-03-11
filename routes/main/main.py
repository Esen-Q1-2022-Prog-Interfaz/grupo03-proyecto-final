from flask import Blueprint, render_template
from sqlalchemy import desc
from db.utils.photos_model import Photo

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template(
        "main/home.html",
        data={
            i: Photo(
                url=f"https://loremflickr.com/320/240?random={i}",
                desc=f"The kitty number {i}",
            )
            for i in range(1, 11)
        },
    )


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


@main.route("/login")
def login():
    return render_template("main/login.html")


@main.route("/register")
def register():
    return render_template("main/register.html")
