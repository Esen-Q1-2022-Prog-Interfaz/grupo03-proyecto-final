<<<<<<< HEAD
from flask import Blueprint, send_file, session, render_template
=======
from flask import Blueprint, render_template
from db.cloud_connection import CloudinaryConnection
from db.utils.photos_model import Photo, PhotoNext
from flask import Blueprint, send_file, session
>>>>>>> origin/administrador
from db.make_excel import create_excel, delete_if_exist
from models.usuarios import Usuarios
from db.db import db
from datetime import datetime

# Vistas
from db.sql_methods import get_view_inscripciones, get_view_registro_academico

# Models
from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios
from models.juntaDirectiva import JuntaDirectiva
from models.contactanos import Contactanos

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
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
        "admin/home.html",
        fotos_data=fotos_data,
        next_act=next_act,
    )


@admin.route("/about")
def about():
    return render_template("admin/about.html")


@admin.route("/activities")
def activities():
    return render_template("admin/activities.html")


@admin.route("/contact")
def contact():
    return render_template("admin/contact.html")


@admin.route("/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")


@admin.route("/download")
def download_excel():
    data = get_view_registro_academico()
    path = create_excel(data)
    if path:
        session["path_excel"] = path
        return send_file(path)
    else:
        return "Hubo un error procesando los datos"


@admin.route("/test")
def db_test():
    if "path_excel" in session:
        delete_if_exist(session["path_excel"])

    newArg = Usuarios(
        "david@hotmial.com",
        "David",
        "Solis",
        4,
        "3434-3433",
        "20200938",
    )
    secArg = Usuarios(
        "20203453@esen.edu.sv",
        "Eleazar",
        "Segovia",
        2,
        "8834-3434",
    )
    thArg = Usuarios(
        "ful@hotmial.com",
        "MEnganito",
        "Fulano",
        3,
        "7444-3233",
        "20200949",
    )
    db.session.add(newArg)
    db.session.add(secArg)
    db.session.add(thArg)
    db.session.commit()

    act_1 = Actividades(
        "Limpiar 1",
        datetime(2022, 4, 6),
        datetime(2045, 11, 12),
        30,
        2,
        3,
        20,
        1,
    )
    act_2 = Actividades(
        "Limpar 2", datetime(2022, 5, 7), datetime(2022, 5, 8), 30, 2, 2, 20, 3
    )
    act_3 = Actividades(
        "Limpar 3", datetime(2022, 4, 6), datetime(2022, 6, 3), 40, 5, 3, 220, True
    )
    db.session.add(act_1)
    db.session.add(act_2)
    db.session.add(act_3)
    db.session.commit()

    for i in range(1, 3):
        for u in range(1, 3):
            ins = Inscripciones(u, i, bool(u % 2), True, 3, 54)
            db.session.add(ins)
            db.session.commit()

    contacto_1 = Contactanos(
        "Ernesto",
        "Cerna",
        "prueba@hotmail.com",
        11110000,
        "asuntointento",
        "mensajeintento",
        True,
    )
    db.session.add(contacto_1)
    db.session.commit()

    # persona_jd_1 = JuntaDirectiva("sofia", "segura", "drectora", "prueba@gmail.com")
    # db.session.add(persona_jd_1)
    # db.session.commit()
    # db.session.add(compra_1)
    # db.session.commit()

    data = Inscripciones.query.all()
    data_2 = get_view_inscripciones()
    data_3 = get_view_registro_academico()
    data_4 = Usuarios.query.all()
    data_5 = Actividades.query.all()
    contactanos = Contactanos.query.all()
    juntaDirectiva = JuntaDirectiva.query.all()
    cupos = Inscripciones.get_cupos_restantes(act_1.idActividad, act_1.cuposTotales)
    return f"""
    <h1>inscripciones</h1>
    {data}
    <h1>usuarios</h1>
    {data_4}
    <h1>actividades</h1>
    {data_5}
    <h1>inscripciones</h1>
    {data}
    <h1>vista insc</h1>
    {data_2}
    <h1>vist reis</h1>
    {data_3}
    <h1>cupos</h1>
    {cupos}
    <h1>compras</h1>
    {contactanos}
    <h1>productos</h1>
    {juntaDirectiva}
<<<<<<< HEAD
   """


=======
   """
>>>>>>> origin/administrador
