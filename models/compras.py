from db.db import db


class Compras(db.Model):  # type: ignore
    """
    Table model de las compras
    Campos:
        idCompra : int
        nombreComprador : str
        apellidoComprador : str
        departamento: str
        municipio: str
        dirección: str
        numeroTel : int
        idProducto: int
        instruccionesExtra: str
    """

    # Campos tabla
    idCompra = db.Column(db.Integer, primary_key=True)
    nombreComprador = db.Column(db.String(50), nullable=False)
    apellidoComprador = db.Column(db.String(50), nullable=False)
    departamento = db.Column(db.String(50), nullable=False)
    municipio = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    numeroTel = db.Column(db.Integer, nullable=False)
    instruccionesExtra = db.Column(db.String(100), nullable=True)

    idProducto = db.Column(
        db.Integer,
        db.ForeignKey("productos.idProducto"),
        nullable=False,
    )

    def __init__(
        self,
        nombreComprador: str,
        apellidoComprador: str,
        departamento: str,
        municipio: str,
        direccion: str,
        numeroTel: int,
        idProducto: int,
        instruccionesExtra: str,
    ) -> None:

        self.nombreComprador = nombreComprador
        self.apellidoComprador = apellidoComprador
        self.departamento = departamento
        self.municipio = municipio
        self.direccion = direccion
        self.numeroTel = numeroTel
        self.idProducto = idProducto
        self.instruccionesExtra = instruccionesExtra

    def __repr__(self) -> str:
        return f"""Compra(
            {self.idCompra}, 
            {self.nombreComprador}, 
            {self.apellidoComprador}, 
            {self.municipio}, 
            {self.direccion}, 
            {self.numeroTel}, 
            {self.idProducto}, 
            {self.instruccionesExtra})""".strip()
