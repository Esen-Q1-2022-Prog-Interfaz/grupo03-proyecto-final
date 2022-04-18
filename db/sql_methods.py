from db.db import db
from db.view_models import VistaRegistro
from models.usuarios import Usuarios
from models.actividades import Actividades
from models.inscripciones import Inscripciones

def get_view_registro_academico() -> list[VistaRegistro]:
    """
    Retorna vista con los campos para inscripciones a alas que estan inscritos:
        carnet : str,
        nombreActividad : str,
        "Nombre y apellido" : str,
        horasSociales : int
    """
    sql_statement = (
        # f"SELECT "
        # # Campos a retornar
        # + f"{DB_USUARIOS}.{CORREO}, "
        # + f"{DB_ACT}.{NAME_ACT}, "
        # + f'CONCAT({DB_USUARIOS}.{NOMBRE}, " ", {DB_USUARIOS}.{APELLIDO}) AS "Nombre y apellido", '
        # + f"{DB_ACT}.{HORAS_SOCIALES}"
        # # joins
        # + f" FROM {DB_INSC} INNER JOIN {DB_ACT} ON {DB_INSC}.{ID_ACT_INSC} = {DB_ACT}.{ID_ACT} "
        # + f"INNER JOIN {DB_USUARIOS} ON {DB_USUARIOS}.{ID_VOL} = {DB_INSC}.{ID_VOL_INSC};"
    )
    result = db.session.execute(sql_statement).fetchall()
    return VistaRegistro.clean_query(result)


def get_view_registro_academico_per_act(idActividad: int):
    query = (
        db.session.query(
            # Campos a ser seleccionados
            Usuarios.correo,
            Usuarios.nombre,
            Usuarios.apellido,
            Actividades.nombreActividad,
            Actividades.tipoHoras,
            Actividades.tipoActividad,
            Actividades.lugarActividad,
            Inscripciones.cantidadKg,
            Inscripciones.evidencia,
            Inscripciones.estadoPago,
            Inscripciones.estadoAsistencia,
        )
        .filter(Actividades.idActividad == idActividad)
        .all()
    )  # type: ignore

    print(query)
    for i in query:
        print(i.nombreActividad)
