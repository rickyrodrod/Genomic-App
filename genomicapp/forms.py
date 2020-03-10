from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):

	antibiotic = StringField('Antibiotic', validators=[DataRequired()])
	organism   = StringField('Organism', validators=[DataRequired()])
	gsps       = StringField('GSPS', validators=[DataRequired()])

	submit     = SubmitField('Exceute Query')
