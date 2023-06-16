from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired()],
                           render_kw={'class': 'form-control shadow-none', 'placeholder': 'Username'})

    password = PasswordField('password',
                             validators=[DataRequired()],
                             render_kw={'class': 'form-control shadow-none', 'placeholder': 'Password'})
