import os
from typing import Union
from db.view_models import VistaRegistro
import pandas as pd
import os


def create_excel(data_vista: list[VistaRegistro], filename = "horas_sociales") -> Union[ str, None]:
    data = [[record.carnet, record.nombre_apellido, record.actividad, record.total_horas ] for record in data_vista]
    df = pd.DataFrame(
        data, columns=["Carnet", "Nombre alumno", "Actividad", "Horas sociales"]
    )
    path = os.getcwd() + "/" + filename + ".xlsx"
    with pd.ExcelWriter(path, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Horas sociales", index=False)
    return path
        
def delete_if_exist(path : str):
    print(f"looking {path}")
    if os.path.exists(path):
        print(f"Removinf file {path}")
        os.remove(path)

