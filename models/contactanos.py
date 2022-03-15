from db.db import db


class Contactanos(db.Model):  # type: ignore
    """
    Table model del contacto
    Campos:
        idContacto : int
        nombre : str
        apellido : str
        correo : str
        numeroTel : int
        asunto : str
        mensaje : str
        estado : boolean
    """

    # Campos tabla
    idContacto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=True)
    asunto = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

    def __init__(
        self,
        nombre: str,
        apellido: str,
        correo: str,
        telefono: int,
        asunto: str,
        mensaje: str,
        estado: bool,
    ) -> None:

        self.nombre = nombre
        self.correo = correo
        self.apellido = apellido
        self.telefono = telefono
        self.asunto = asunto
        self.mensaje = mensaje
        self.estado = estado

    def __repr__(self) -> str:
        return f"""Contactanos(
            {self.idContacto}, 
            {self.nombre}, 
            {self.apellido}, 
            {self.telefono}, 
            {self.correo},
            {self.asunto}, 
            {self.mensaje}, 
            {self.estado})""".strip()
