from flask import Blueprint, render_template
from db.cloud_connection import CloudinaryConnection
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
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


@main.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check is user esta agregado
        pass  
    return render_template("main/login.html", form=form)


@main.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Agregar user a db
        pass
    return render_template("main/register.html", form=form)
