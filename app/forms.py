# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    discription = TextAreaField('Movie Discription',validators=[InputRequired])
    poster = FileField('Movie Poster',validators=[FileRequired(),
                                                  FileAllowed(['jpeg','jpg','png'],
                                                               'Images Only!')])