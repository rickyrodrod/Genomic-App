from flask import render_template
from genomicapp import app
from genomicapp.forms import QueryForm
@app.route("/")
def home():
	form = QueryForm()
	return render_template("home.html", title='Home', form=form)
