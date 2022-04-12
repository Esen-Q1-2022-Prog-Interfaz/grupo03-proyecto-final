from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from db.cloud_connection import CloudinaryConnection
from forms.form_contactanos import FormContactanos
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from db.utils.photos_model import Photo, PhotoNext
from models.inscripciones import Inscripciones
from utils_app.bcrypt import bcrypt
from models.juntaDirectiva import JuntaDirectiva
from models.actividades import Actividades
from models.usuarios import Usuarios
from models.contactanos import Contactanos
from db.db import db
from datetime import date

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
    actividadesActivas = Actividades.query.filter_by(estado=2).all()
    return render_template(
        "main/home.html",
        fotos_data=fotos_data,
        next_act=next_act,
        user=current_user,
        actividadesActivas=actividadesActivas
    )


@main.route("/about")
def about():
    JDList = JuntaDirectiva.query.all()
    return render_template("main/about.html", JDList=JDList, user=current_user)


@main.route("/activities")
def activities():
    activitiesList = Actividades.query.all()
    return render_template("main/activities.html", activitiesList=activitiesList, user=current_user)

@main.route("/activities/inscripcion", methods=["GET", "POST"])
@login_required
def inscripcion(nombreAct):
    idVoluntario=current_user.idVoluntario
    idActividad= nombreAct
    estadoAsistencia=1
    estadoPago=2
    cantidadKg=0
    horastotales=0
    evidencia=1
    newIns = Inscripciones(idVoluntario, idActividad, estadoAsistencia, estadoPago, cantidadKg, horastotales, evidencia)
    db.session.add(newIns)
    db.session.commit()
    return redirect(url_for("main.activities", nombreAct=nombreAct))
    

@main.route("/contact", methods=["POST", "GET"])
def contact():
    form = FormContactanos()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido =  form.apellido.data
        telefono = form.telefono.data
        text_area = form.text_area.data
        newMessage = Contactanos(nombre, apellido, telefono, text_area, False)        
        db.session.add(newMessage)
        db.session.commit()
        return redirect(url_for("main.contact"))

    return render_template("main/contact.html", form=form, user=current_user)


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

                return redirect(url_for("main.home"))
    return render_template("main/login.html", form=form, user=current_user)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

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
        carrera = form.carrera.data
        anno = [int(i) for i in list(correo)[0:4]]
        annoo = int(''.join(map(str, anno)))
        print(type(annoo))
        
        newUser = Usuarios(correo, hashed_password, nombre, apellido, telefono, "NA", "NA", carrera, annoo)
        db.session.add(newUser)
        db.session.commit()
        
        return redirect (url_for("main.login"))
    return render_template("main/register.html", form=form, user=current_user)

@main.route("/profile")
@login_required
def profile():
    return render_template("main/profile.html", user=current_user)
