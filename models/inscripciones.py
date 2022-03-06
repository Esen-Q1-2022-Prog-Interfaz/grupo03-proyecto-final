from db.db import db


class Inscripciones(db.Model):  # type: ignore
    """
    Table model de inscripciones:
    Campos:
        idVoluntario : int
        idActividad : int
        estado : bool
        pago : bool
        horasSociales : int
        cantidadKg : int
    """

    # Campos tabla
    idInscripcion = db.Column(db.Integer, primary_key=True)
    idVoluntario = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.idVoluntario"),
        nullable=False,
    )
    idActividad = db.Column(
        db.Integer,
        db.ForeignKey("actividades.idActividad"),
        nullable=False,
    )
    estado = db.Column(db.Boolean, nullable=False)
    pago = db.Column(db.Boolean, nullable=False)
    horasSociales = db.Column(db.Integer, nullable=False)
    cantidadKg = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        idVoluntario: int,
        idActividad: int,
        estado: bool,
        pago: bool,
        horasSociales: int,
        cantidadKg: int,
    ) -> None:

        self.idActividad = idActividad
        self.idVoluntario = idVoluntario
        self.estado = estado
        self.pago = pago
        self.horasSociales = horasSociales
        self.cantidadKg = cantidadKg

    def __repr__(self) -> str:
        return f"""
        {self.idInscripcion},
        {self.idActividad},
        {self.idVoluntario},
        {self.estado},
        {self.pago},
        {self.horasSociales},
        {self.cantidadKg}
        """.strip()
