from datetime import datetime
from typing import Union
from __future__ import annotations


class VistaUsuarios:
    """
    Model de la vista usuarios:
        Campos:
            idVoluntario: int
            actividad: str
            fechaInicio: datetime
            fechaFinal: datetime
            horas_por_actividad: int
            status: int
    """

    def __init__(
        self,
        idVoluntario: int,
        actividad: str,
        fechaInicio: datetime,
        fechaFinal: datetime,
        horas_por_actividad: int,
        status: Union[bool, int],
    ) -> None:

        self.idVoluntario = idVoluntario
        self.actividad = actividad
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.horas_por_actividad = horas_por_actividad
        self.status: str = "Finalizada" if status else "Cancelada"

    @classmethod
    def clean_query(cls, raw_query: list[tuple]) -> list[VistaUsuarios]:
        """Limpia el query retornando registros del modelo VistaUsuarios"""
        return [cls(*raw_actvividad) for raw_actvividad in raw_query]

    def __repr__(self) -> str:
        return f"""
        VistaUsuario(
            {self.idVoluntario}, 
            {self.actividad}, 
            {self.fechaInicio}, 
            {self.fechaFinal}, 
            {self.horas_por_actividad}, 
            {self.status}
        )""".strip()


class VistaRegistro:
    """
    Model de la vista para registro academico:
        Campos:
            carnet : str,
            actividad : str,
            nombre_apellido : str,
            total_horas : int
    """

    def __init__(
        self,
        carnet: str,
        actividad: str,
        nombre_apellido: str,
        total_horas: int,
    ) -> None:
        self.carnet = carnet
        self.actividad = actividad
        self.nombre_apellido = nombre_apellido
        self.total_horas = total_horas

    @classmethod
    def clean_query(cls, raw_query: list[tuple]) -> list[VistaRegistro]:
        """Limpia el query retornando registros del modelo VistaRegistro"""
        return [cls(*raw_vol) for raw_vol in raw_query]

    def __repr__(self) -> str:
        return f"""
        VistaReistro(
            {self.carnet},
            {self.actividad},
            {self.nombre_apellido},
            {self.total_horas}
        )
        """.strip()
