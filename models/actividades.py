from db.connections import db
from datetime import datetime


class Actividades(db.Model):  # type: ignore
    """
    Table model de las actividades
    Campos:
        nombreActividad : str
        fechaInicio : datetime
        fechaFinal : datetime
        cantidadVoluntarios : int
        horasSociales : int
    """

    # Campos tabla
    idActividad = db.Column(db.Integer, primary_key=True)
    nombreActividad = db.Column(db.String(50), nullable=False)
    fechaInicio = db.Column(db.DateTime(), nullable=False)
    fechaFinal = db.Column(db.DateTime(), nullable=False)
    # TODO: cantidad de voluntarios es un campo calculado? i mean: COUNT("los alumnos inscritos a la actividad")
    cantidadVoluntarios = db.Column(db.Integer, nullable=False)
    horasSociales = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        nombreActividad: str,
        fechaInicio: datetime,
        fechaFinal: datetime,
        cantidadVoluntarios: int,
        horasSociales: int,
    ) -> None:

        self.nombreActividad = nombreActividad
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.cantidadVoluntarios = cantidadVoluntarios
        self.horasSociales = horasSociales

    def __repr__(self) -> str:
        # TODO:clean this comment. Ese strip es para que quede ordenado el string tras ponerlo de esa forma mas leible
        return f"""
        Actividad(
        {self.idActividad},
        {self.nombreActividad},
        {self.fechaInicio},
        {self.fechaFinal},
        {self.cantidadVoluntarios},
        {self.horasSociales}
        )
        """.strip()
