from flask import Blueprint, redirect, render_template_string, request, send_file, session, render_template
from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from db.utils.photos_model import Photo, PhotoNext
from flask import Blueprint, send_file, session
from db.make_excel import create_excel, delete_if_exist
from models.usuarios import Usuarios
from db.db import db
from datetime import datetime
from random import randint
from models.datos import Datos
from forms.form_addJD import FormAddJD
from forms.form_updateActivity import FormUpdateActivity
from forms.form_updateJD import FormUpdateJD
from forms.form_addActividad import FormAddActivity
from models.actividades import Actividades

# Vistas
from db.sql_methods import get_view_inscripciones, get_view_registro_academico

# Models
from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios
from models.juntaDirectiva import JuntaDirectiva
from models.contactanos import Contactanos
from utils_app.cryptography import CryptographyToken

datetime.today().isoformat()

admin = Blueprint("admin", __name__, url_prefix="/admin")

images_random_ids = [
    "1MgiiLYn9wPtCEN5hBHwvJejEhFt_R10X",
    "16mHFP9gq-McNvphRBZbYM5QYwGHteabx",
    "1pF6jyqFSYLXOvFWxL9wLdehLPUym2qOV"
]

STRING_SHARING = "https://drive.google.com/uc?id"

def add_Act():
    act_1 = Actividades("no se aun", "no se", 2, "sepa hudas", 1, datetime(2022, 5, 7), datetime(2022, 7, 7), 23, 34,  1)
    act_2 = Actividades("no se aun", "no se 2", 2, "sepa hudas", 1, datetime(2022, 5, 7), datetime(2022, 7, 7), 23, 34,  1)

    act_3 = Actividades("no se aun", "no se 3", 2, "sepa hudas", 1, datetime(2022, 5, 7), datetime(2022, 7, 7), 23, 34,  1)
    
    db.session.add(act_1)
    db.session.add(act_2)
    db.session.add(act_3)
    db.session.commit()


def get_image_id_from_link(link : str) -> str:
    id_photo = ""
    split_string = link.replace("https://drive.google.com/", "").split("/")
    id_photo = split_string[-2]
    return id_photo

@admin.route("/")
def home():
    add_Act()
    if "path_excel" in session:
        delete_if_exist(session["path_excel"])

    fotos_data = {
        i: Photo(
            url= STRING_SHARING + "=" + images_random_ids[randint(0, 2)],
            desc=f"",
        )
        for i in range(1, 11)
    }

    next_act = {
        i: PhotoNext(
            STRING_SHARING + "=" + images_random_ids[randint(0, 2)],
            f"No se {i}",
            0,
        )
        for i in range(1, 13)
    }
    print(next_act)

    return render_template(
        "admin/home.html",
        fotos_data=fotos_data,
        next_act=next_act,
        user=current_user,
    )



@admin.route("/about")
def about():
    return render_template("admin/about.html", user=current_user,)


@admin.route("/activities")
def activities():
    return render_template("admin/activities.html", user=current_user,)

@admin.route("/activities/inscripcion", methods=["GET", "POST"])
@login_required
def inscripcion(nombreAct):
    idVoluntario=current_user.idVoluntario
    idActividad= nombreAct
    estadoAsistencia=1
    estadoPago=2
    cantidadKg=0
    horastotales=0
    evidencia=1
    newIns = Inscripciones(idVoluntario, idActividad, estadoAsistencia, estadoPago, cantidadKg, horastotales)
    db.session.add(newIns)
    db.session.commit()
    return redirect(url_for("main.activities", nombreAct=nombreAct))
    


@admin.route("/contact")
def contact():
    return render_template("admin/contact.html", user=current_user,)


@admin.route("/dashboard")
def dashboard():
    if current_user.departamento == "Admin" or 1 == 1:
        # VoluntariosFull = Usuarios.query.filter_by(Usuarios.departamento != "Baja").all()
        # MiembrosFull2 = Usuarios.query.filter_by(departamento == "NA").all()
        
        MiembrosFull = Usuarios.query.filter_by(cargo="miembro").all()
        VoluntarioFull = Usuarios.query.filter_by(cargo="NA").all()
        JDFull = JuntaDirectiva.query.all()
        InscripcionesFull = Inscripciones.query.all()
        ActividadesFull = Actividades.query.all()
        MessagesFull = Contactanos.query.all()
        return render_template("admin/dashboard.html", VoluntarioFull=VoluntarioFull,  MiembrosFull=MiembrosFull, JDFull=JDFull, InscripcionesFull=InscripcionesFull, ActividadesFull=ActividadesFull, MessagesFull=MessagesFull, user=current_user)
    
    return redirect(url_for("main.home"))


@admin.route("/delete/user/<int:idVoluntario>")
def deleteVoluntario(idVoluntario):
    selectedUser = Usuarios.query.filter_by(idVoluntario=idVoluntario).first()
    correo = selectedUser.correo
    contrasenna = selectedUser.contrasenna
    nombre = selectedUser.nombre
    apellido = selectedUser.apellido
    telefono = selectedUser.telefono
    carrera = selectedUser.carrera
    anno = selectedUser.anno
    departamento="Baja"
    
    selectedUser.correo = correo
    selectedUser.contrasenna = contrasenna
    selectedUser.nombre = nombre
    selectedUser.apellido = apellido
    selectedUser.telefono = telefono
    selectedUser.carrera = carrera
    selectedUser.anno = anno
    selectedUser.departamento = departamento
    db.session.add(selectedUser)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idVoluntario=idVoluntario))

@admin.route("/Upgrade/user/<int:idVoluntario>", methods=["POST", "GET"])
def hacerMiembro(idVoluntario):
    if request.method == "POST":
        selectedUser = Usuarios.query.filter_by(idVoluntario=idVoluntario).first()
        correo = selectedUser.correo
        contrasenna = selectedUser.contrasenna
        nombre = selectedUser.nombre
        apellido = selectedUser.apellido
        telefono = selectedUser.telefono
        carrera = selectedUser.carrera
        anno = selectedUser.anno
        departamento=request.form.get("position")
        cargo = "miembro"
        
        selectedUser.correo = correo
        selectedUser.contrasenna = contrasenna
        selectedUser.nombre = nombre
        selectedUser.apellido = apellido
        selectedUser.telefono = telefono
        selectedUser.carrera = carrera
        selectedUser.anno = anno
        selectedUser.departamento = departamento
        selectedUser.cargo = cargo
        db.session.add(selectedUser)
        db.session.commit()
        return redirect(url_for("admin.dashboard", idVoluntario=idVoluntario))
    else:
        return redirect(url_for("admin.dashboard", idVoluntario=idVoluntario))

@admin.route("/NewActivity", methods=["POST", "GET"])
def addActivity():
    user=current_user
    form  = FormAddActivity()
    if form.validate_on_submit():
        descripcion = form.descripcion.data
        nombre = form.nombre.data
        tipoActividad = form.tipoActividad.data
        lugarActividad = form.lugarActividad.data
        tipoHoras = form.tipoHoras.data
        fechaInicio = form.fechaInicio.data
        fechaFinal = form.fechaFinal.data
        horasSociales = form.horasSociales.data
        cuposTotales = form.cuposTotales.data
        estado = 1
        newAct = Actividades(
            descripcion,
            nombre,
            tipoActividad, 
            lugarActividad,
            tipoHoras,
            fechaInicio,
            fechaFinal,
            horasSociales,
            cuposTotales,
            estado,
            )
        db.session.add(newAct)
        db.session.commit()
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/activities/newActivity.html", form=form, user=user)

@admin.route("/updateActivity", methods=["POST", "GET"])
def updateActivity():
    user=current_user
    form  = FormAddActivity()
    if form.validate_on_submit():
        descripcion = form.descripcion.data
        nombre = form.nombre.data
        tipoActividad = form.tipoActividad.data
        lugarActividad = form.lugarActividad.data
        tipoHoras = form.tipoHoras.data
        fechaInicio = form.fechaInicio.data
        fechaFinal = form.fechaFinal.data
        horasSociales = form.horasSociales.data
        cuposTotales = form.cuposTotales.data
        estado = 1
        newAct = Actividades(
            descripcion,
            nombre,
            tipoActividad, 
            lugarActividad,
            tipoHoras,
            fechaInicio,
            fechaFinal,
            horasSociales,
            cuposTotales,
            estado,
            )
        db.session.add(newAct)
        db.session.commit()
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/activities/updateActivity.html", form=form, user=user)



@admin.route("/NewJD", methods=["POST", "GET"])
def addJD():
    user = current_user
    form  = FormAddJD()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        cargo = form.cargo.data
        correo = form.correo.data
        link = form.link.data
        newJD = JuntaDirectiva(
            nombre,
            apellido, 
            cargo,
            correo,
            link,
            )
        db.session.add(newJD)
        db.session.commit()
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/JD/newJD.html", form=form, user=user)


@admin.route("/downgrade/user/<int:idVoluntario>")
def hacerVoluntario(idVoluntario):
    selectedUser = Usuarios.query.filter_by(idVoluntario=idVoluntario).first()
    correo = selectedUser.correo
    contrasenna = selectedUser.contrasenna
    nombre = selectedUser.nombre
    apellido = selectedUser.apellido
    telefono = selectedUser.telefono
    carrera = selectedUser.carrera
    anno = selectedUser.anno
    departamento="NA"
    cargo="NA"
    
    selectedUser.correo = correo
    selectedUser.contrasenna = contrasenna
    selectedUser.nombre = nombre
    selectedUser.apellido = apellido
    selectedUser.telefono = telefono
    selectedUser.carrera = carrera
    selectedUser.anno = anno
    selectedUser.departamento = departamento
    selectedUser.cargo = cargo
    db.session.add(selectedUser)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idVoluntario=idVoluntario))


@admin.route("/delete/junta/<int:idPersona>")
def deleteJD(idPersona):
    selectedUserJD = JuntaDirectiva.query.filter_by(idPersona=idPersona).first()
    db.session.delete(selectedUserJD)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idPersona=idPersona))

@admin.route("/delete/actividad/<int:idActividad>")
def deleteActividad(idActividad):
    selectedActividad = Actividades.query.filter_by(idActividad=idActividad).first()
    db.session.delete(selectedActividad)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idActividad=idActividad))

@admin.route("/changeStatus/mensaje/<int:idContacto>")
def changeStatusMessage(idContacto):
    selectedMessage = Contactanos.query.filter_by(idContacto=idContacto).first()
    # id = selectedMessage.idContacto
    nombre = selectedMessage.nombre
    apellido = selectedMessage.apellido
    telefono = selectedMessage.telefono
    mensaje = selectedMessage.mensaje
    if selectedMessage.estado==0:
        newStatus=1
    else:
        newStatus=0
    
    selectedMessage.nombre = nombre
    selectedMessage.apellido = apellido
    selectedMessage.telefono = telefono
    selectedMessage.mensaje = mensaje
    selectedMessage.estado = newStatus
    db.session.add(selectedMessage)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idContacto=idContacto))


@admin.route("/delete/mensaje/<int:idContacto>")
def deleteMessage(idContacto):
    selectedMessage = Contactanos.query.filter_by(idContacto=idContacto).first()
    db.session.delete(selectedMessage)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idContacto=idContacto))


@admin.route("/download")
def download_excel():
    data = get_view_registro_academico()
    path = create_excel(data)
    if path:
        session["path_excel"] = path
        return send_file(path)
    else:
        return "Hubo un error procesando los datos"

def generate_link_reset_password(id, correo_init):
    cryptography_tool = CryptographyToken()
    return f"/reset/password/{cryptography_tool.encrypt_token(id)}/{cryptography_tool.encrypt_token(correo_init)}"


@admin.route(f"/reset/password/<id>/<correo>", methods=["POST", "GET"])
def generate_link(id, correo):
    link = generate_link_reset_password(id, correo)
    return render_template("admin/reset_link.html", user=current_user, link=link)

# @admin.route("/test")
# def db_test():
#     if "path_excel" in session:
#         delete_if_exist(session["path_excel"])

#     newArg = Usuarios(
#         "david@hotmial.com",
#         ""
#         "David",
#         "Solis",
#         "3434-3433",
#         20200938,
#     )
#     secArg = Usuarios(
#         "20203453@esen.edu.sv",
#         "Eleazar",
#         "Segovia",
#         2,
#         "8834-3434",
#     )
#     thArg = Usuarios(
#         "ful@hotmial.com",
#         "MEnganito",
#         "Fulano",
#         3,
#         "7444-3233",
#         "20200949",
#     )
#     db.session.add(newArg)
#     db.session.add(secArg)
#     db.session.add(thArg)
#     db.session.commit()

#     act_1 = Actividades(
#         "Limpiar 1",
#         datetime(2022, 4, 6),
#         datetime(2045, 11, 12),
#         30,
#         2,
#         3,
#         20,
#         1,
#     )
#     act_2 = Actividades(
#         "Limpar 2", datetime(2022, 5, 7), datetime(2022, 5, 8), 30, 2, 2, 20, 3
#     )
#     act_3 = Actividades(
#         "Limpar 3", datetime(2022, 4, 6), datetime(2022, 6, 3), 40, 5, 3, 220, True
#     )
#     db.session.add(act_1)
#     db.session.add(act_2)
#     db.session.add(act_3)
#     db.session.commit()

#     for i in range(1, 3):
#         for u in range(1, 3):
#             ins = Inscripciones(u, i, bool(u % 2), True, 3, 54)
#             db.session.add(ins)
#             db.session.commit()

#     contacto_1 = Contactanos(
#         "Ernesto",
#         "Cerna",
#         "prueba@hotmail.com",
#         11110000,
#         "asuntointento",
#         "mensajeintento",
#         True,
#     )
#     db.session.add(contacto_1)
#     db.session.commit()

#     # persona_jd_1 = JuntaDirectiva("sofia", "segura", "drectora", "prueba@gmail.com")
#     # db.session.add(persona_jd_1)
#     # db.session.commit()
#     # db.session.add(compra_1)
#     # db.session.commit()

#     data = Inscripciones.query.all()
#     data_2 = get_view_inscripciones()
#     data_3 = get_view_registro_academico()
#     data_4 = Usuarios.query.all()
#     data_5 = Actividades.query.all()
#     contactanos = Contactanos.query.all()
#     juntaDirectiva = JuntaDirectiva.query.all()
#     cupos = Inscripciones.get_cupos_restantes(act_1.idActividad, act_1.cuposTotales)
#     return f"""
#     <h1>inscripciones</h1>
#     {data}
#     <h1>usuarios</h1>
#     {data_4}
#     <h1>actividades</h1>
#     {data_5}
#     <h1>inscripciones</h1>
#     {data}
#     <h1>vista insc</h1>
#     {data_2}
#     <h1>vist reis</h1>
#     {data_3}
#     <h1>cupos</h1>
#     {cupos}
#     <h1>compras</h1>
#     {contactanos}
#     <h1>productos</h1>
#     {juntaDirectiva}
#    """


