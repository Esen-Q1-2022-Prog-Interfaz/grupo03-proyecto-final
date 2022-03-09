from db.db import db
from models.actividades import Actividades


class Inscripciones(db.Model):  # type: ignore
    """
    Table model de inscripciones:
    Campos:
        idVoluntario : int
        idActividad : int
        estado : bool
        pago : bool
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
    cantidadKg = db.Column(db.Float, nullable=True)
    evidencia = db.Column(db.String(20), nullable=False)

    def __init__(
        self,
        idVoluntario: int,
        idActividad: int,
        estado: bool,
        pago: bool,
        cantidadKg: float,
    ) -> None:

        self.idActividad = idActividad
        self.idVoluntario = idVoluntario
        self.estado = estado
        self.pago = pago
        self.cantidadKg = cantidadKg
        actividad = Actividades.get_activity(self.idActividad)
        if actividad != 3:
            self.evidencia = "---"
        else:
            self.evidencia = str(False)

    def __repr__(self) -> str:
        return f"""
    Inscripciones(
        {self.idInscripcion},
        {self.idActividad},
        {self.idVoluntario},
        {self.estado},
        {self.pago},
        {self.cantidadKg},
        {self.evidencia}
    )
    """.strip()

    def get_horas_sociales(self):
        """Retorna horas sociales + (horasKg por cantidad recogida)"""
        actitivdad: Actividades = Actividades.query.get(self.idActividad)
        return actitivdad.horasSociales + (
            actitivdad.horasKg or 0 * self.cantidadKg or 0
        )

    @classmethod
    def get_cupos_restantes(cls, idActividad, cuposTotales) -> int:
        """Retorna los cupos restantes de una actividad"""
        cupos_llenos = len(cls.query.filter_by(idActividad=idActividad).all())
        return cuposTotales - cupos_llenos
