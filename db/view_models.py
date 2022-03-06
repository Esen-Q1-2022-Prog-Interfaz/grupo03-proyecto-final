from datetime import datetime
from typing import Union


class VistaUsuarios:
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
    def clean_query(cls, raw_query: list[tuple]):
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
    def __init__(
        self,
        carnet,
        actividad,
        nombre_apellido,
        total_horas,
    ) -> None:
        self.carnet = carnet
        self.actividad = actividad
        self.nombre_apellido = nombre_apellido
        self.total_horas = total_horas

    @classmethod
    def clean_query(cls, raw_query: list[tuple]):
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