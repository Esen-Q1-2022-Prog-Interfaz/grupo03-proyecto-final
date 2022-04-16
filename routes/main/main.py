from random import randint
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
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

images_random_ids = [
    "1MgiiLYn9wPtCEN5hBHwvJejEhFt_R10X",
    "16mHFP9gq-McNvphRBZbYM5QYwGHteabx",
    "1pF6jyqFSYLXOvFWxL9wLdehLPUym2qOV"
]

STRING_SHARING = "https://drive.google.com/uc?id"

def get_image_id_from_link(link : str) -> str:
    id_photo = ""
    split_string = link.replace("https://drive.google.com/", "").split("/")
    id_photo = split_string[-2]
    return id_photo


@main.route("/")
def home():

    fotos_data = {
        i: Photo(
            url= STRING_SHARING + "=" + images_random_ids[randint(0, 2)],
            desc=f"The kitty number {i}",
        )
        for i in range(1, 11)
    }

    next_act = {
        i: PhotoNext(
            STRING_SHARING + "=" + images_random_ids[randint(0, 2)],
            f"No se {i}",
            0
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
    ins_act = db.session.query(Actividades.idActividad).join(Inscripciones).join(Usuarios).filter(Inscripciones.idVoluntario == current_user.idVoluntario).all() if current_user.is_authenticated else []
    inscrip_acti = [act.idActividad for act in ins_act]
    return render_template("main/activities.html", activitiesList=activitiesList, user=current_user, ins_act=inscrip_acti)

@main.route("/activities/inscripcion/<string:idActividad>", methods=["GET", "POST"])
@login_required
def inscripcion(idActividad):
    idVoluntario=current_user.idVoluntario
    estadoAsistencia=1
    estadoPago=2
    cantidadKg=0
    horastotales=0
    print(idActividad)
    newIns = Inscripciones(idVoluntario, idActividad, estadoAsistencia, estadoPago, cantidadKg, horastotales)
    print(newIns)
    db.session.add(newIns)
    db.session.commit()
    return redirect(url_for("main.activities", idActividad=idActividad))
    

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
        return redirect(url_for("main.contact", is_posted=True))
    
    is_posted = request.args.get("is_posted") if "is_posted" in request.args else False
    return render_template("main/contact.html", form=form, user=current_user, is_posted=is_posted)


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
    actividades_dict = {}
    ins_act = []
    inscripciones = Inscripciones.query.filter_by(idVoluntario=current_user.idVoluntario).all()
    for ins in inscripciones:
        if ins.idActividad not in actividades_dict:
            activity = Actividades.query.get(ins.idActividad)
            actividades_dict[ins.idActividad] = activity
        ins_act.append((ins, actividades_dict[ins.idActividad]))
    return render_template("main/profile.html", user=current_user, ins_act=ins_act)


