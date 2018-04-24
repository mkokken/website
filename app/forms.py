from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FloatField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from math import pi 

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class CalculateForm(FlaskForm):
    area = StringField('Beschikbare dakoppervlak in m<sup>2', validators=[DataRequired()])
    jaar = StringField('Hoeveel jaren wil je meenemen in het advies? (twee geeft de beste optimalisatie)', validators=[DataRequired()], default =2)
    energieverbruik = StringField('Energie verbruik per jaar in kWh',validators=[DataRequired()])
    submit = SubmitField('Creer advies')
    
class TestForm(FlaskForm):
    bedrijfsnaam = StringField('Bedrijfsnaam:', validators = [DataRequired()])
    postcode = StringField('Postcode:', validators = [DataRequired()])
    tbedrijf = SelectField('Type bedrijf:', choices = [('mvh','Melkveehouderij'), ('akb','Akkerbouw'), ('tnb', 'Tuinbouw')], validators = [DataRequired()])
    a_pers = StringField('Aantal persoonsleden:', validators = [DataRequired()])
    omzet = StringField('Gemiddelde jaaromzet (x 1000):', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    phone = StringField('Telefoonnummer:', validators = [DataRequired()])
    submit = SubmitField('Ga door')
    
class InputForm(FlaskForm): 
     A = FloatField( 
         label='amplitude (m)', default=1.0, 
         validators=[validators.InputRequired()]) 
     b = FloatField( 
         label='damping factor (kg/s)', default=0, 
         validators=[validators.InputRequired()]) 
     w = FloatField( 
         label='frequency (1/s)', default=2*pi, 
         validators=[validators.InputRequired()]) 
     T = FloatField( 
         label='time interval (s)', default=18, 
         validators=[validators.InputRequired()]) 

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')