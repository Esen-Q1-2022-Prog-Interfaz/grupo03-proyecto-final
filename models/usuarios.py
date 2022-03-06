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
    anno = db.Column(db.DateTime)
    telefono = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

    def __init__(
        self,
        carnet: str,
        nombre: str,
        apellido: str,
        anno: datetime,
        telefono: str,
        correo: str,
    ) -> None:

        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno
        self.telefono = telefono
        self.correo = correo

    def __repr__(self) -> str:
        return f"""Usuario(
            {self.idVoluntario}, 
            {self.carnet}, 
            {self.nombre}, 
            {self.apellido}, 
            {self.anno}, 
            {self.telefono}, 
            {self.correo})""".strip()

    def get_carnet(self):
        carnet: str
        try:
            carnet = self.correo[:7]
        except Exception:
            carnet = "None"
        return carnet

    @staticmethod
    def get_carnet_from_correo(correo: str):
        return correo[:7]
