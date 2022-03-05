from db.connections import db

class Usuario(db.Model):  # type: ignore
    """
    Data model para tabla Usuario
    Campos de tabla:

    idVoluntario : int
    carnet : str
    nombre : str
    apellido : str
    anno : DateTime
    telefono : str
    correo : str
    """

    # Campos tabla
    idVoluntario = db.Column(db.Ingeter, primary_key=True)
    carnet = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    # TODO: fix name, pongo anno o year ?
    anno = db.Column(db.DateTime)
    telefono = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

    def __init__(
        self,
        idVoluntario,
        carnet,
        nombre,
        apellido,
        anno,
        telefono,
        correo,
    ) -> None:

        self.idVoluntario = idVoluntario
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
