from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.db import db
from db.sql_methods import get_view_inscripciones, get_view_registrp_academico

from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios

app = Flask(__name__)
app.config.from_object("config.BaseConfig")
SQLAlchemy(app)


# Es una muestra de como se usa
@app.route("/")
def home():
    newArg = Usuarios(
        "20200938",
        "David",
        "Solis",
        datetime(2022, 4, 23),
        "3434-3433",
        "david@hotmial.com",
    )
    secArg = Usuarios(
        "20200948",
        "Eleazar",
        "Segovia",
        datetime(2023, 5, 13),
        "8834-3434",
        "generic@hotmial.com",
    )
    thArg = Usuarios(
        "20200949",
        "MEnganito",
        "Fulano",
        datetime(2025, 4, 5),
        "7444-3233",
        "ful@hotmial.com",
    )
    db.session.add(newArg)
    db.session.add(secArg)
    db.session.add(thArg)
    db.session.commit()

    act_1 = Actividades(
        "Limpiar 1", datetime(2022, 4, 6), datetime(2045, 11, 12)
    )
    act_2 = Actividades(
        "Limpar 2", datetime(2022, 5, 7), datetime(2022, 5, 8)
    )
    act_3 = Actividades(
        "Limpar 3", datetime(2022, 4, 6), datetime(2022, 6, 3)
    )
    db.session.add(act_1)
    db.session.add(act_2)
    db.session.add(act_3)
    db.session.commit()

    for i in range(1,3):
        for u in range(1,3):
            ins = Inscripciones(u, i, bool(u%2), True, 54, 23)
            db.session.add(ins)
            db.session.commit()

    data = Inscripciones.query.all()
    data_2 = get_view_inscripciones()
    data_3 = get_view_registrp_academico()
    data_4 = Usuarios.query.all()
    data_5 = Actividades.query.all()

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
   """


with app.app_context():
    db.create_all()

if "__main__" == __name__:
    app.run(debug=True)
