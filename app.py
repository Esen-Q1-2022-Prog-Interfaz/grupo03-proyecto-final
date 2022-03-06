from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.db import db
from db.sql_methods import get_view_inscripciones

from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios

app = Flask(__name__)
app.config.from_object("config.BaseConfig")
SQLAlchemy(app)

# TODO: Borren esta weaaaaaaa
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
        "20200938",
        "Eleazar",
        "Segovia",
        datetime(2023, 5, 13),
        "8834-3434",
        "david@hotmial.com",
    )
    thArg = Usuarios(
        "20200938",
        "MEnganito",
        "Fulano",
        datetime(2025, 4, 5),
        "7444-3233",
        "david@hotmial.com",
    )
    # db.session.add(newArg)
    # db.session.add(secArg)
    # db.session.add(thArg)
    # db.session.commit()

    act_1 = Actividades(
        "Limpiar 1", datetime(2022, 4, 6), datetime(2045, 11, 12)
    )
    # db.session.add(act_1)
    # db.session.commit()

    newInscrip = Inscripciones(2, 1, False, True, 54, 23)
    # db.session.add(newInscrip)
    # db.session.commit()

    data = Inscripciones.query.all()
    data_2 = get_view_inscripciones()

    return f"Fallo? {data} {data_2}"


with app.app_context():
    db.create_all()

if "__main__" == __name__:
    app.run(debug=True)
