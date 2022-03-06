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
    #Mejor dejamos horasSociales en Actividades, lo escribimos una vez por actividad y aca solo es una foranea
    #Si no, tendríamos que validar cada registro if IdActividad=1, horassociales=60, por ejemplo
    cantidadKg = db.Column(db.Float, nullable=True)
    #HorasPorKilo
    
    #Evaluar TipoActividad para asignar HorasTotales
    #HorasTotales: HorasTipo1+(CantidadKg*HorasPorKilo)
    #Agregar Columna: Evidencia (si TipoActividad=1 o 2, NA; Si TipoActividad=3, evaluar(De forma natural: "NO", Pero se puede cambiar a "Sí"))

    def __init__(
        self,
        idVoluntario: int,
        idActividad: int,
        estado: bool,
        pago: bool,
        horasSociales: int,
        cantidadKg: float,
    ) -> None:

        self.idActividad = idActividad
        self.idVoluntario = idVoluntario
        self.estado = estado
        self.pago = pago
        self.horasSociales = horasSociales
        self.cantidadKg = cantidadKg

    def __repr__(self) -> str:
        return f"""
        Inscripciones(
            {self.idInscripcion},
            {self.idActividad},
            {self.idVoluntario},
            {self.estado},
            {self.pago},
            {self.horasSociales},
            {self.cantidadKg}
        )
        """.strip()
