from flask import Blueprint, render_template, redirect, url_for
from db.cloud_connection import CloudinaryConnection
from forms.form_contactanos import FormContactanos
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from db.utils.photos_model import Photo, PhotoNext
from utils.bcrypt import bcrypt
from models.juntaDirectiva import JuntaDirectiva
from models.actividades import Actividades
from models.usuarios import Usuarios
from models.contactanos import Contactanos
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


@main.route("/contact", methods=["POST", "GET"])
def contact():
    form = FormContactanos()
    if form.validate_on_submit():
        # testin if form is being submitted
        print("SUBMITED")
        #test end
        nombre = form.nombre.data
        apellido =  form.apellido.data
        telefono = form.telefono.data
        text_area = form.text_area.data
        newMessage = Contactanos(nombre, apellido, telefono, text_area, 0)        
        db.session.add(newMessage)
        db.session.commit()
        return redirect (url_for("main.contact"))
    # testin if form is being submitted
    else:
        print("not submitted yet")

    return render_template("main/contact.html", form=form)


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
