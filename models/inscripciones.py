from db.db import db


class Inscripciones(db.Model):  # type: ignore
    """
    Table model de inscripciones:
    Campos:
        idVoluntario : int
        idActividad : int
        estado : bool
        pago : bool
        cantidadKg : int
        Evidencia: boolean
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
    cantidadKg = db.Column(db.Float, nullable=True)
    evidencia = db.Column(db.Boolean(), nullable=False)

    def __init__(
        self,
        idVoluntario: int,
        idActividad: int,
        estado: bool,
        pago: bool,
        cantidadKg: float,
        evidencia: bool,
    ) -> None:

        self.idActividad = idActividad
        self.idVoluntario = idVoluntario
        self.estado = estado
        self.pago = pago
        self.cantidadKg = cantidadKg
        self.evidencia = evidencia

    def __repr__(self) -> str:
        return f"""
        Inscripciones(
            {self.idInscripcion},
            {self.idActividad},
            {self.idVoluntario},
            {self.estado},
            {self.pago},
            {self.horasSociales},
            {self.cantidadKg},
            {self.evidencia}
        )
        """.strip()
