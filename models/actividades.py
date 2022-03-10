from db.db import db
from datetime import datetime


class Actividades(db.Model):  # type: ignore
    """
    Table model de las actividades
    Campos:
        nombreActividad : str
        fechaInicio : datetime
        fechaFinal : datetime
        horasSociales : int
        horasKg : int
        tipoActividad: int
        cuposTotales: int
        estado : str
    """

    # Campos tabla
    idActividad = db.Column(db.Integer, primary_key=True)
    nombreActividad = db.Column(db.String(50), nullable=False)
    fechaInicio = db.Column(db.DateTime, nullable=False)
    fechaFinal = db.Column(db.DateTime, nullable=False)
    horasSociales = db.Column(db.Integer, nullable=True)
    horasKg = db.Column(db.Integer, nullable=True)
    tipoActividad = db.Column(db.Integer, nullable=False)
    cuposTotales = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), nullable=False)


    def __init__(
        self,
        nombreActividad: str,
        fechaInicio: datetime,
        fechaFinal: datetime,
        horasSociales: int,
        horasKg: int,
        tipoActividad: int,
        cuposTotales: int,
        estado : str
    ) -> None:

        self.nombreActividad = nombreActividad
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.horasSociales = horasSociales
        self.horasKg = horasKg
        self.tipoActividad = tipoActividad
        self.cuposTotales = cuposTotales
        self.estado = estado

    def __repr__(self) -> str:

        return f"""
        Actividad(
        {self.idActividad},
        {self.nombreActividad},
        {self.fechaInicio},
        {self.fechaFinal},
        {self.horasSociales},
        {self.horasKg},
        {self.tipoActividad},
        {self.cuposTotales},
        {self.estado}
        )
        """.strip()

    @classmethod
    def get_activity(cls, id : int) -> int:
        result =  cls.query.get(id) 
        return result.tipoActividad
