from datetime import datetime


class VistaUsuarios:
    def __init__(
        self,
        idVoluntario,
        actividad,
        fechaInicio,
        fechaFinal,
        horas_por_actividad,
        status,
    ) -> None:
        self.idVoluntario: int = idVoluntario
        self.actividad: str = actividad
        self.fechaInicio: datetime = fechaInicio
        self.fechaFinal: datetime = fechaFinal
        self.horas_por_actividad: int = horas_por_actividad
        self.status: int = status

    @classmethod
    def clean_query(cls, raw_query: list):
        actividades = []
        for raw_actvividad in raw_query:
            actividades.append(
                cls(*raw_actvividad)
            )
        return actividades

    def __repr__(self) -> str:
        return f"VistaUsuario({self.idVoluntario}, {self.actividad}, {self.fechaInicio}, {self.fechaFinal}, {self.horas_por_actividad}, {self.status})"
