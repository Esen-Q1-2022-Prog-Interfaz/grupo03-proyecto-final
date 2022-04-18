from __future__ import annotations

class VistaRegistro:
    """
    Model de la vista para registro academico:
        Campos:
            carnet : str,
            nombre_apellido : str,
            lugar : str,
            tipo_actividad : str
            tipo_horas : str,
            fecha_inicio : str,
            fecha_final : str
    """

    def __init__(
        self,
        correo: str,
        actividad: str,
        nombre_apellido: str,
        tipo_horas : str, 
        total_horas: int,
    ) -> None:
        self.carnet = VistaRegistro.get_carnet(correo)
        self.actividad = actividad
        self.nombre_apellido = nombre_apellido
        self.total_horas = tipo_horas
        self.total_horas = total_horas

    @classmethod
    def clean_query(cls, query):
        pass
        

    @staticmethod
    def get_carnet(correo_: str):
        carnet = "NA"
        if correo_.endswith("@esen.edu.sv"):
            carnet = correo_.removesuffix("@esen.edu.sv")
        return carnet


    def __repr__(self) -> str:
        return f"""
        VistaReistro(
            {self.carnet},
            {self.actividad},
            {self.nombre_apellido},
            {self.total_horas}
        )
        """.strip()
