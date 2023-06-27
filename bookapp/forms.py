from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from flask_wtf.file import _FileField,FileAllowed,FileRequired


class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your full name is required")])
    email = StringField("Your Email",validators=[Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm password',validators=[EqualTo('password',message='confirm password must be equal to password')])
    btn = SubmitField("Sign up!")


class profileForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your full name is required")])
    pix=_FileField('Display Picture',validators=[FileRequired(),FileAllowed(['jpg','png'],'image only')])
    btn = SubmitField("update profile")
  
    
    
    
    
    
     
    

