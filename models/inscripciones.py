from db.db import db
from models.actividades import Actividades


class Inscripciones(db.Model):  # type: ignore
    """
    Table model de inscripciones:
    Campos:
        idVoluntario : int
        idActividad : int
        estadoInicial : int
        estadoFinal: int
        pago : int
        cantidadKg : float
        evidencia: int
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
    estadoInicial = db.Column(db.Integer, nullable=False)
    estadoFinal = db.Column(db.Integer, nullable=False)
    pago = db.Column(db.Integer, nullable=False)
    cantidadKg = db.Column(db.Float, nullable=True)
    evidencia = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        idVoluntario: int,
        idActividad: int,
        estadoInicial: int,
        estadoFinal: int,
        pago: int,
        cantidadKg: float,
    ) -> None:

        self.idActividad = idActividad
        self.idVoluntario = idVoluntario
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.pago = pago
        self.cantidadKg = cantidadKg
        
        actividad = Actividades.get_activity(self.idActividad)
        #SOLIS    #SOLIS    #SOLIS    #SOLIS    #SOLIS    #SOLIS    #SOLIS    #SOLIS    
        #¿Qué está guardado en "actividad"? Porque estás metiendole actividades.X where idActividad==idActividad, qué es X?
        
        if actividad != 3: #Let TipoActividad=3 means its webinar
            self.evidencia = 0 #Let 0=No Aplica
        else:
            self.evidencia = 1 #Let 1=No Entregada

    def __repr__(self) -> str:
        return f"""
    Inscripciones(
        {self.idInscripcion},
        {self.idActividad},
        {self.idVoluntario},
        {self.estadoInicial},
        {self.estadoFinal}
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
