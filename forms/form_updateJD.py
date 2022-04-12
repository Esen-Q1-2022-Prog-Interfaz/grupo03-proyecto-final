from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length


class FormContactanos(FlaskForm):
    nombre = StringField(
        "Nombre",
        validators=[InputRequired(), Length(min=2, max=10)],
        render_kw={"placeholder": "Ingresa el nombre"},
    )

    apellido = StringField(
        "Apellido",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa el apellido"},
    )

    cargo = StringField(
        "Cargo",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa el cargo"},
    )

    correo = StringField(
        "correo",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Ingresa el correo"},
    )
    
    link = StringField(
        "link",
        validators=[InputRequired(), Length(min=3, max=1000)],
        render_kw={"placeholder": "Ingresa el link de la foto"},
    )

    submit = SubmitField("Enviar")
