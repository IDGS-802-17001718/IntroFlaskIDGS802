from wtforms import Form
from wtforms import StringField, EmailField, SelectField, RadioField, IntegerField
from wtforms import validators

class UserForm(Form):
    nombre=StringField("nombre",[
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    email=EmailField("correo",[validators.Email(message="Ingrese un correo valido")])
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    """ materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','ING')])
    radios= RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')]) """
    edad=IntegerField("edad",[validators.number_range(min=1, max=20, message='Valor no valido')])