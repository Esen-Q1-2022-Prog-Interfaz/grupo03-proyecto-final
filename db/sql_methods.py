from db.db import db
from db.view_models import VistaRegistro, VistaUsuarios

DB_USUARIOS = "`Usuarios`"
ID_VOL = "`idVoluntario`"
NOMBRE = "`nombre`"
APELLIDO = "`apellido`"
ANNO = "`anno`"
TELEFONO = "`telefono`"
CORREO = "`correo`"
CARNET = "`carnet`"

DB_ACT = "`Actividades`"
ID_ACT = "`idActividad`"
NAME_ACT = "`nombreActividad`"
FECHA_IN = "`fechaInicio`"
FECHA_FIN = "`fechaFinal`"
HORAS_SOCIALES = "`horasSociales`"
HORAS_KG = "`horasKg`"
TIPO_ACT = "`tipoActividad`"
CUPOS_TOTALES = "`cuposTotales`"
ESTADO_ACT = "`estado`"

DB_INSC = "`Inscripciones`"
ID_VOL_INSC = "`idVoluntario`"
ID_ACT_INSC = "`idActividad`"
ESTADO = "`estado`"
PAGO = "`pago`"
CANT_KG = "`cantidadKg`"
EVIDENCIA = "`evidencia`"


def get_view_inscripciones() -> list[VistaUsuarios]:
    """
    Retorna vista con los campos para inscripciones a alas que estan inscritos:
        idVoluntario : int,
        nombreActividad : str,
        fechaInicio : datetime
        fechaFinal : datetime,
        horasSociales : int,
        estado : bool
    """
    sql_statement = (
        f"SELECT "
        # Valores a retornar
        + f"{DB_USUARIOS}.{ID_VOL}, "
        + f"{DB_ACT}.{NAME_ACT}, "
        + f"{DB_ACT}.{FECHA_IN}, "
        + f"{DB_ACT}.{FECHA_FIN}, "
        + f"{DB_ACT}.{HORAS_SOCIALES}, "
        + f"{DB_INSC}.{ESTADO}"
        # Los joins
        + f" FROM {DB_INSC} INNER JOIN {DB_ACT} ON {DB_INSC}.{ID_ACT_INSC} = {DB_ACT}.{ID_ACT} "
        + f"INNER JOIN {DB_USUARIOS} ON {DB_USUARIOS}.{ID_VOL} = {DB_INSC}.{ID_VOL_INSC};"
    )
    result = db.session.execute(sql_statement).fetchall()
    return VistaUsuarios.clean_query(result)


def get_view_registro_academico() -> list[VistaRegistro]:
    """
    Retorna vista con los campos para inscripciones a alas que estan inscritos:
        carnet : str,
        nombreActividad : str,
        "Nombre y apellido" : str,
        horasSociales : int
    """
    sql_statement = (
        f"SELECT "
        # Campos a retornar
        + f"{DB_USUARIOS}.{CARNET}, "
        + f"{DB_ACT}.{NAME_ACT}, "
        + f'CONCAT({DB_USUARIOS}.{NOMBRE}, " ", {DB_USUARIOS}.{APELLIDO}) AS "Nombre y apellido", '
        + f"{DB_ACT}.{HORAS_SOCIALES}"
        # joins
        + f" FROM {DB_INSC} INNER JOIN {DB_ACT} ON {DB_INSC}.{ID_ACT_INSC} = {DB_ACT}.{ID_ACT} "
        + f"INNER JOIN {DB_USUARIOS} ON {DB_USUARIOS}.{ID_VOL} = {DB_INSC}.{ID_VOL_INSC};"
    )
    result = db.session.execute(sql_statement).fetchall()
    return VistaRegistro.clean_query(result)
