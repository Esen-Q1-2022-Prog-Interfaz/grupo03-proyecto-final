from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.connections import db
from models.actividades import Actividades
from models.inscripciones import Inscripciones
from models.usuarios import Usuarios

app = Flask(__name__)
app.config.from_object("config.BaseConfig")
SQLAlchemy(app)

# TODO: Borren esta weaaaaaaa
# TODO: Delete esta route, es solo para ver si el SqlAlchemy works :), y of course it works
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
    db.session.add(newArg)
    db.session.add(secArg)
    db.session.add(thArg)
    db.session.commit()

    act_1 = Actividades(
        "Limpiar 1", datetime(2022, 4, 6), datetime(2045, 11, 12), 34, 45
    )
    db.session.add(act_1)
    db.session.commit()

    newInscrip = Inscripciones(2, 1, False, True)
    db.session.add(newInscrip)
    db.session.commit()

    return "Fallo?"


with app.app_context():
    db.create_all()

if "__main__" == __name__:
    app.run(debug=True)
