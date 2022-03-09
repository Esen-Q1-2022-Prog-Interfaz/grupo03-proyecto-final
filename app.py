from datetime import datetime
from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
from flask import session
from db.db import db
from db.make_excel import create_excel, delete_if_exist
from db.sql_methods import get_view_inscripciones, get_view_registro_academico

from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios
from models.juntaDirectiva import juntaDirectiva
from models.contactanos import contactanos
from models.productos import productos
from models.compras import compras


app = Flask(__name__)
app.config.from_object("config.BaseConfig")
SQLAlchemy(app)


# Todo: BORRAR ANTES DE MERGE
# Es una muestra de como se usa
@app.route("/")
def home():
    if "path_excel" in session:
        delete_if_exist(session["path_excel"])
        session.pop("path_excel")

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
        "En pie",
    )
    act_2 = Actividades(
        "Limpar 2", 
        datetime(2022, 5, 7), 
        datetime(2022, 5, 8), 
        30, 
        2, 
        2, 
        20, 
        "En pie"
    )
    act_3 = Actividades(
        "Limpar 3", 
        datetime(2022, 4, 6), 
        datetime(2022, 6, 3), 
        40, 
        5, 
        3, 
        220, 
        "En pie"
    )
    db.session.add(act_1)
    db.session.add(act_2)
    db.session.add(act_3)
    db.session.commit()

    for i in range(1, 3):
        for u in range(1, 3):
            ins = Inscripciones(u, i, bool(u % 2), True, 54)
            db.session.add(ins)
            db.session.commit()

    contacto_1=contactanos(
        "Ernesto",
        "Cerna",
        "prueba@hotmail.com",
        11110000,
        "asuntointento",
        "mensajeintento",
        1
    )
    db.session.ad(contacto_1)
    db.session.commit()
    
    persona_jd_1=juntaDirectiva(
        "sofia",
        "segura",
        "drectora",
        "prueba@gmail.com"
    )
    db.session.ad(persona_jd_1)
    db.session.commit()
    
    prod_1=productos(
        "producto 1",
        "Descripcion producto 1",
        "linkimagen"
    )
    db.session.ad(prod_1)
    db.session.commit()
    
    compra_1=compras(
        "ernesto",
        "cerna",
        "Santa Ana",
        "Santa Ana",
        "Casa 1",
        1111000,
        1,
        "instruccion"
    )
    db.session.ad(compra_1)
    db.session.commit()
    
    
    data = Inscripciones.query.all()
    data_2 = get_view_inscripciones()
    data_3 = get_view_registro_academico()
    data_4 = Usuarios.query.all()
    data_5 = Actividades.query.all()
    contactanos = contactanos.query.all()
    juntaDirectiva = juntaDirectiva.query.all()
    productos = productos.query.all()
    compras = compras.query.all()
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
    <h1>Junta Directiva</h1>
    {productos}
    <h1>Productos</h1>
    {compras}
   """


@app.route("/download")
def get_excel_file():
    data = get_view_registro_academico()
    path = create_excel(data)
    if path:
        session["path_excel"] = path
        return send_file(path, as_attachment=True)
    else:
        return "Hubo un error procesando los datos"


with app.app_context():
    db.create_all()

if "__main__" == __name__:
    app.run(debug=True)
