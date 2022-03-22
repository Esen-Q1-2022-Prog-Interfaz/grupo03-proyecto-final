from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user
from db.cloud_connection import CloudinaryConnection
from forms.form_contactanos import FormContactanos
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from db.utils.photos_model import Photo, PhotoNext
from utils_app.bcrypt import bcrypt
from models.juntaDirectiva import JuntaDirectiva
from models.actividades import Actividades
from models.usuarios import Usuarios
from db.db import db

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
    JDList = JuntaDirectiva.query.all()
    return render_template("main/about.html", JDList=JDList)


@main.route("/activities")
def activities():
    activitiesList = Actividades.query.all()
    return render_template("main/activities.html", activitiesList=activitiesList)


@main.route("/contact")
def contact():
    form = FormContactanos()
    return render_template("main/contact.html", form=form)


@main.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        correo = form.correo.data
        contra = form.contrasenna.data
        user = Usuarios.query.filter_by(correo=correo).first()
        if user:
            if bcrypt.check_password_hash(user.contrasenna, contra):
                login_user(user)
                # TODO: poner en lugar de iniciar sesion nombre del usuario logeado, o sea modificar el html 
        pass  
    return render_template("main/login.html", form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        correo = form.correo.data
        nombre = form.nombre.data
        apellido =  form.apellido.data
        telefono = form.telefono.data
        password = form.contrasenna.data
        hashed_password = bcrypt.generate_password_hash(password)
        newUser = Usuarios(correo, hashed_password, nombre, apellido, telefono, "NA") 
        db.session.add(newUser)
        db.session.commit()
        return redirect (url_for("main.login"))
    return render_template("main/register.html", form=form)
