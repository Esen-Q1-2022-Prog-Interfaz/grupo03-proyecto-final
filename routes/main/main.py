from flask import Blueprint, render_template
from db.cloud_connection import CloudinaryConnection
from db.utils.photos_model import Photo, PhotoNext

main = Blueprint("main", __name__)


@main.route("/")
def home():
    cloud = CloudinaryConnection.get_connection()
    img_url, data = cloud.get_image()

    fotos_data = {
        i: Photo(
            url=img_url,
            desc=f"The kitty number {i}",
        )
        for i in range(1, 11)
    }

    next_act = {
        i: PhotoNext(
            img_url,
            f"No se {i}",
            0,
        )
        for i in range(1, 13)
    }

    return render_template(
        "main/home.html",
        fotos_data=fotos_data,
        next_act=next_act,
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


@main.route("/profile")
def profile():
    return render_template("main/profile.html")
