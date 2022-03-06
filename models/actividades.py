from db.db import db
from datetime import datetime


class Actividades(db.Model):  # type: ignore
    """
    Table model de las actividades
    Campos:
        nombreActividad : str
        fechaInicio : datetime
        fechaFinal : datetime
    """

    # Campos tabla
    idActividad = db.Column(db.Integer, primary_key=True)
    nombreActividad = db.Column(db.String(50), nullable=False)
    fechaInicio = db.Column(db.DateTime(), nullable=False)
    fechaFinal = db.Column(db.DateTime(), nullable=False) #Propongo tener un campo Cupos
    #Porque permite printear en la tabla "Quedan x cupos" comparando los registros en "Inscripciones" con actividades.CantidadVoluntarios
    #Agregar un campo TipoActividad (1:presencial, 2:reciclaje, 3:virtual)

    def __init__(
        self,
        nombreActividad: str,
        fechaInicio: datetime,
        fechaFinal: datetime,
    ) -> None:

        self.nombreActividad = nombreActividad
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal

    def __repr__(self) -> str:

        return f"""
        Actividad(
        {self.idActividad},
        {self.nombreActividad},
        {self.fechaInicio},
        {self.fechaFinal},
        )
        """.strip()
