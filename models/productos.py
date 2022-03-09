from db.db import db

class productos(db.Model):  # type: ignore
    """
    Table model de los productos
    Campos:
        idProducto : int
        nombreProducto : str
        descripcionProducto : str
        imagen : str
    """

    # Campos tabla
    idProducto = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(50), nullable=False)
    descripcionProducto = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(500), nullable=False)

    def __init__(
        self,
        nombreProducto: str,
        descripcionProducto: str,
        imagen: str,
    ) -> None:

        self.nombreProducto = nombreProducto
        self.descripcionProducto = descripcionProducto
        self.imagen = imagen

    def __repr__(self) -> str:
        return f"""Usuario(
            {self.idProducto}, 
            {self.nombreProducto}, 
            {self.descripcionProducto}, 
            {self.imagen})""".strip()
