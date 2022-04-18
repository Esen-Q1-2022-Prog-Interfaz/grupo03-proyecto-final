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
from db.sql_methods import get_view_registro_academico

# Models
from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios
from models.juntaDirectiva import JuntaDirectiva
from models.contactanos import Contactanos
from utils_app.cryptography import CryptographyToken
from utils_app.random_images import STRING_SHARING, get_image_id_from_link, get_random_images_list


admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
def home():
    img_random = get_random_images_list()
    
    fotos_data = {
        i: Photo(
            url=STRING_SHARING + "=" + i,
            desc=f"",
        )
        for i in img_random
    }

    next_act = {
        i: PhotoNext(
            STRING_SHARING + "=" + i, f"No se {i}", 0
        )
        for i in img_random
    }

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
    idVoluntario=current_user.idVoluntario # type: ignore
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
    if current_user.departamento == "Admin" or 1 == 1: # type: ignore
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

@admin.route("/updateActivity/<int:idActividad>", methods=["POST", "GET"])
def updateActivity(idActividad):
    user = current_user
    currentActividad = Actividades.query.filter_by(idActividad=idActividad).first()
    form  = FormUpdateActivity(actividades=currentActividad)
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
        Estado = form.Estado.data
        
        currentActividad.descripcion = descripcion
        currentActividad.nombre = nombre
        currentActividad.tipoActividad = tipoActividad
        currentActividad.lugarActividad = lugarActividad
        currentActividad.tipoHoras = tipoHoras
        currentActividad.fechaInicio = fechaInicio
        currentActividad.fechaFinal = fechaFinal
        currentActividad.horasSociales = horasSociales
        currentActividad.cuposTotales = cuposTotales
        currentActividad.Estado = Estado
        db.session.add(currentActividad)
        db.session.commit()
        return redirect(url_for("admin.dashboard", form=form, user=user, currentActividad=currentActividad, idActividad=idActividad))
    # form.descripcion.data=currentActividad.dewscric
    return render_template("admin/activities/updateActivity.html", form=form, user=user, currentActividad=currentActividad, idActividad=idActividad)


@admin.route("/NewJD", methods=["POST", "GET"])
def addJD():
    user = current_user
    form  = FormAddJD()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        cargo = form.cargo.data
        correo = form.correo.data
        link = STRING_SHARING +  "=" + get_image_id_from_link(form.link.data)
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



@admin.route("/updateJD/<int:idPersona>", methods=["POST", "GET"])
def updateJD(idPersona):
    user = current_user
    currentJD = JuntaDirectiva.query.filter_by(idPersona=idPersona).first()
    form  = FormUpdateJD(juntadirectiva=currentJD)
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        cargo = form.cargo.data
        correo = form.correo.data
        link = STRING_SHARING +  "=" + get_image_id_from_link(form.link.data)
        currentJD.nombre = nombre
        currentJD.apellido = apellido
        currentJD.cargo = cargo
        currentJD.correo = correo
        currentJD.link = link
        db.session.add(currentJD)
        db.session.commit()
        return redirect(url_for("admin.dashboard", form=form, user=user, idPersona=idPersona, currentJD=currentJD))
    return render_template("admin/JD/updateJD.html", form=form, user=user, idPersona=idPersona, currentJD=currentJD)


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
    JuntaDirectiva.query.filter_by(idPersona=idPersona).delete()
    db.session.commit()
    return redirect(url_for("admin.dashboard", idPersona=idPersona))

@admin.route("/delete/actividad/<int:idActividad>")
def deleteActividad(idActividad):
    Actividades.query.filter_by(idActividad=idActividad).delete()
    Inscripciones.query.filter_by(idActividad = idActividad).delete()
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
    selectedMessage = Contactanos.query.get(idContacto)
    db.session.delete(selectedMessage)
    db.session.commit()
    return redirect(url_for("admin.dashboard", idContacto=idContacto))


@admin.route("/download")
def download_excel():
    if "path_excel" in session:
        delete_if_exist(session["path_excel"])

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

