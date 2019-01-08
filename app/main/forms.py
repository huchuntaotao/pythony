#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import DataRequired,Length,Email,Regexp, EqualTo
from ..models import User

class NameForm(FlaskForm):
    name = StringField("What's your name?",validators=[DataRequired()])
    submit=SubmitField('Submit')
    
    
class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Length(1,128),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in.") #复选框
    submit=SubmitField('Submit')
    
    
class RegisterForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Length(1,128),Email()])
    username = StringField("Username",validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                         'Usernames must have only letters,numbers, dots or underscores')])
    password = PasswordField("Password",validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    password2 = PasswordField("Password2",validators=[DataRequired()])
    submit=SubmitField('Register')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
        
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
