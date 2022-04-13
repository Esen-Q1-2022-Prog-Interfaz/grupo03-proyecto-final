from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length

TipoActividad=[
    ("1", "Reciclaje"),
    ("2", "Limpieza"),
    ("3", "Capacitaciones"),
    ("4", "Otro"), 
]

TipoHoras=[
    ("1", "Medioambientales"),
    ("2", "Normales"),
    ("3", "Administrativas"),
]

# Estados=[
#     ("1", "En progreso"),
#     ("2", "Terminada"),
#     ("3", "Cancelada"),
# ]

class FormContactanos(FlaskForm):
    descripcion = StringField(
        "descripcion",
        validators=[InputRequired(), Length(min=2, max=2000)],
        render_kw={"placeholder": "Ingresa la descripcion"},
    )

    nombre = StringField(
        "Nombre",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa el nombre de la actividad"},
    )

    tipoActividad = SelectField(
        label="Tipo de Actividad",
        validators=[InputRequired()],
        choices= TipoActividad,
        render_kw={"placeholder":"Ingresa el tipo de actividad"}
    )

    lugarActividad = StringField(
        "Lugar",
        validators=[InputRequired(), Length(min=3, max=100)],
        render_kw={"placeholder": "Ingresa el lugar de realización de la actividad"},
    )
    
    tipoHoras = SelectField(
        label="Tipo de Horas",
        validators=[InputRequired()],
        choices= TipoHoras,
        render_kw={"placeholder":"Ingresa el tipo de horas de la actividad"}
    )
    
    fechaInicio = IntegerField(
        "Horas Sociales",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa las horas sociales asistencia o por kilo, según aplique"},
    )
    
# En las fechas podemos implementar un datepicker en el html para evitar que pongan la fecha con mal formato
    fechaInicio = IntegerField(
        "Fecha de Inicio",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa la fecha de inicio"},
    )

# En las fechas podemos implementar un datepicker en el html para evitar que pongan la fecha con mal formato
    fechaFinal = IntegerField(
        "Fecha de fin",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa la fecha de finalización"},
    )
    
    horasSociales = IntegerField(
        "Horas Sociales",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa las horas sociales asistencia o por kilo, según aplique"},
    )
    
    cuposTotales = IntegerField(
        "Cupos totales",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa los cupos totales para la actividad"},
    )
# # Estado predeterminado: 1
#     Estado = SelectField(
#         label="Estado",
#         validators=[InputRequired()],
#         choices= Estados,
#         render_kw={"placeholder":"Ingresa el estado de la actividad"}
#     )

    submit = SubmitField("Enviar")