from typing import Union
from db.db import db
from datetime import datetime


class Usuarios(db.Model):  # type: ignore
    """
    Table model de los Usuarios
    Campos:
        carnet : str
        nombre : str
        apellido : str
        anno : DateTime
        telefono : str
        correo : str
    """

    # Campos tabla
    idVoluntario = db.Column(db.Integer, primary_key=True)
    carnet = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    anno = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

    def __init__(
        self,
        correo: str,
        nombre: str,
        apellido: str,
        anno: int,
        telefono: str,
        carnet: Union[str, None] = None,
    ) -> None:

        self.nombre = nombre
        self.correo = correo
        self.apellido = apellido
        self.anno = anno
        self.telefono = telefono
        self.carnet = self.get_carnet(carnet)

    def __repr__(self) -> str:
        return f"""Usuario(
            {self.idVoluntario}, 
            {self.carnet}, 
            {self.nombre}, 
            {self.apellido}, 
            {self.anno}, 
            {self.telefono}, 
            {self.correo})""".strip()

    def get_carnet(self, carnet_: Union[str, None]):
        carnet: str
        if bool(carnet_) and not self.correo.endswith("@esen.edu.sv"):
            carnet = carnet_
        else:
            try:
                carnet = self.correo[:7]
            except Exception:
                carnet = "None"
        return carnet
