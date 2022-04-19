from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length
from wtforms.fields import StringField, SubmitField, SelectField, PasswordField, IntegerField, DateField


evidencias=[
    ("1", "Enviada"),
    ("2", "No enviada"),
    ("3", "NA"),
]

asistencias=[
    ("1", "Asistió"),
    ("2", "No asistió"),
    ("3", "Canceló"),
]

pagos=[
    ("1", "Pagado"),
    ("2", "No pagado"),
    ("3", "NA"),
]

class FormUpdateInsc(FlaskForm):
    asistencia = SelectField(
        "Estado asistencia",
        validators=[InputRequired()],
        choices= asistencias,
        render_kw={"placeholder": "Ingresa estado asistencia"},
    )

    pago = SelectField(
        "Estado pago",
        validators=[InputRequired()],
        choices= pagos,
        render_kw={"placeholder": "Ingresa estado pago"},
    )

    cantidadKg = IntegerField(
        label="Cantidad kg",
        validators=[InputRequired()],
        render_kw={"placeholder":"Ingresa cantidad"}
    )

    evidencia = SelectField(
        "Evidencia",
        validators=[InputRequired()],
        choices= evidencias,
        render_kw={"placeholder": "Ingresa estado evidencia"},
    )
    

# # En las fechas podemos implementar un datepicker en el html para evitar que pongan la fecha con mal formato
#     fechaFinal = DateField(
#         "Fecha de finalización",
#          format='%Y-%m-%d',
#         validators=[InputRequired()],
#         render_kw={"placeholder": "Ingresa la fecha de finalización"},
#     )
    
#     horasSociales = IntegerField(
#         "Horas Sociales",
#         validators=[InputRequired()],
#         render_kw={"placeholder": "Ingresa las horas sociales asistencia o por kilo, según aplique"},
#     )
    
#     cuposTotales = IntegerField(
#         "Cupos totales",
#         validators=[InputRequired()],
#         render_kw={"placeholder": "Ingresa los cupos totales para la actividad"},
#     )
    
#     Estado = SelectField(
#         label="Estado",
#         validators=[InputRequired()],
#         choices= Estados,
#         render_kw={"placeholder":"Ingresa el estado de la actividad"}
#     )

    submit = SubmitField("Modificar")
