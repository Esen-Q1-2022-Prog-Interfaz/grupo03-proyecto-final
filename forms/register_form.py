from flask_wtf import FlaskForm
from nbformat import ValidationError
from wtforms.fields import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo
from models.usuarios import Usuarios

YEARS_UNI = [
    ("1", "Primer año"),
    ("2", "Segundo año"),
    ("3", "Tercer año"),
    ("4", "Cuarto año"),
    ("5", "Quinto año"),
]

class RegisterForm(FlaskForm):
    correo = StringField(
        label="Correo",
        validators=[
            InputRequired(),
            Length(min=15, max=25)
        ],
        render_kw={"placeholder":"Ingresa tu correo institucional"}
    )

    nombre = StringField(
        label="Nombre",
        validators=[
            InputRequired(),
            Length(max=100),
        ],
        render_kw={"placeholder":"Ingresa tu nombre"}
    )

    apellido = StringField(
        label="Apellido",
        validators=[
            InputRequired(),
            Length(max=100),
        ],
        render_kw={"placeholder":"Ingresa tu apellido"}
    )

    telefono = StringField(
        label="Telefono +503",
        validators=[
            InputRequired(),
            Length(max=8),
        ],
        render_kw={"placeholder":"Ingresa tu telefono"}
    )
    
    year_uni = SelectField(
        label="Año universitario",
        validators=[
            InputRequired()
        ],
        choices=YEARS_UNI,
        render_kw={"placeholder":"Ingresa tu año unversisario"}
    )

    contrasenna = PasswordField(
        label="Contraseña",
        validators=[
            InputRequired(),
            Length(min=2, max=15)
        ],
        render_kw={"placeholder":"Ingresa tu contraseña"}
    )

    contrasenna_2 = PasswordField(
        label="Contraseña",
        validators=[
            InputRequired(),
            Length(min=2, max=15),
            EqualTo("contrasenna", message='Las contraseñas son distintas')

        ],
        render_kw={"placeholder":"Ingresa de nuevo tu contraseña"}
    )

    submit = SubmitField(label="Registrarse")

    def validate_correo(self, correo):
        correo_typed : str = correo.data
        if not correo_typed.endswith("@esen.edu.sv"):
            raise ValidationError("No eres alumno de la ESEN")
        elif Usuarios.query.filter_by(correo=correo).first():    
            raise ValidationError(f"Ya hay un correo {correo_typed} registrado")