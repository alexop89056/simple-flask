from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length


class EditForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(3, 20)],
                       render_kw={'class': 'form-control shadow-none', 'placeholder': 'Name'})

    username = StringField('Username',
                           validators=[DataRequired()],
                           render_kw={'class': 'form-control shadow-none', 'placeholder': 'Username'})

    password = PasswordField('Password',
                             render_kw={'class': 'form-control shadow-none', 'placeholder': 'Password'})

    role = SelectField('Role', choices=[('student', 'Student'), ('employer', 'Employer'), ('admin', 'Admin')],
                       render_kw={'class': 'form-select shadow-none'})

    contact = StringField('Contact',
                          validators=[DataRequired()],
                          render_kw={'class': 'form-control shadow-none', 'placeholder': 'Contact'})
