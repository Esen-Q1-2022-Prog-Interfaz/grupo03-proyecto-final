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
FECHA_IN = "`fechaInicio`"
FECHA_FIN = "`fechaFinal`"
NAME_ACT = "`nombreActividad`"

DB_INSC = "`Inscripciones`"

ID_VOL_INSC ="`idVoluntario`"
ID_ACT_INSC = "`idActividad`"
ESTADO = "`estado`"
PAGO = "`pago`"
HORAS_SOCIALES = "`horasSociales`"
CANT_KG = "`cantidadKg`"

def get_view_inscripciones() -> list[VistaUsuarios]:
    sql_statement = (
        f"SELECT "
        # Valores a retornar
        + f"{DB_USUARIOS}.{ID_VOL}, "
        + f"{DB_ACT}.{NAME_ACT},"
        + f"{DB_ACT}.{FECHA_IN},"
        + f"{DB_ACT}.{FECHA_FIN},"
        + f"{DB_INSC}.{HORAS_SOCIALES},"
        + f"{DB_INSC}.{ESTADO}"
        # Los joins
        + f" FROM {DB_INSC} INNER JOIN {DB_ACT} ON {DB_INSC}.{ID_ACT_INSC} = {DB_ACT}.{ID_ACT} "
        + f"INNER JOIN {DB_USUARIOS} ON {DB_USUARIOS}.{ID_VOL} = {DB_INSC}.{ID_VOL_INSC};"
    )
    result = db.session.execute(sql_statement).fetchall()
    return VistaUsuarios.clean_query(result)

def get_view_registrp_academico():
    sql_statement = (
        f"SELECT "
        # Campos a retornar
        + f"{DB_USUARIOS}.{CARNET}, "
        + f"{DB_ACT}.{NAME_ACT}, "
        + f'({DB_USUARIOS}.{NOMBRE} + {DB_USUARIOS}.{APELLIDO}) as "Nombre y apellido",'
        + f'{DB_INSC}.{HORAS_SOCIALES}'
        #joins
        + f" FROM {DB_INSC} INNER JOIN {DB_ACT} ON {DB_INSC}.{ID_ACT_INSC} = {DB_ACT}.{ID_ACT} "
        + f"INNER JOIN {DB_USUARIOS} ON {DB_USUARIOS}.{ID_VOL} = {DB_INSC}.{ID_VOL_INSC};"
    )
    result = db.session.executee(sql_statement).fetch_all()
    return VistaRegistro.clean_query(result)