from typing import Union
from db.db import db
from datetime import datetime


class Usuarios(db.Model):  # type: ignore
    """
    Table model de los Usuarios
    Campos:
        carnet : str
        nombre : str
        contrasenna : str
        apellido : str
        anno : int
        telefono : str
        correo : str
    """

    # Campos tabla
    idVoluntario = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), nullable=False)
    contrasenna = db.Column(db.String(100), nullable= False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    departamento = db.Column(db.String(50), nullable=False)

    def __init__(
        self,
        correo: str,
        contrasenna: Union[str, bytes],
        nombre: str,
        apellido: str,
        telefono: str,
        departamento: str,
    ) -> None:

        self.correo = correo
        self.contrasenna = contrasenna
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.departamento = departamento

    def __repr__(self) -> str:
        return f"""Usuario(
            {self.idVoluntario}, 
            {self.carnet}, 
            {self.contrasenna},
            {self.nombre}, 
            {self.apellido}, 
            {self.telefono}, 
            {self.departamento},
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
