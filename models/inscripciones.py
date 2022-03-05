from db.connections import db


class Inscripcion:
    """
    Data model de tabla inscripcion
    Campos: 
    

    """
    idInscripcion = db.Column(db.Integer, primary_key=True)
    idVoluntario = db.Column(db.Integer, db.ForeignKey(
        'usuarios.idvoluntario'), nullable=False)
    idActividad = db.Column(db.Integer, db.ForeignKey(
        'actividades.idactividad'), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    pago = db.Column(db.Boolean, nullable=False)

    def __init__(
        self,
        idInstripcion,
        idVoluntario,
        idActividad,
        estado,
        pago,
    ) -> None:
        self.idActividad = idActividad
        self.idInscripcion = idInstripcion
        self.idVoluntario = idVoluntario
        self.estado = estado
        self.pago = pago

    def __repr__(self) -> str:
        return f"""
        {self.idInscripcion},
        {self.idActividad},
        {self.idVoluntario},
        {self.estado},
        {self.pago}
        """.strip()
