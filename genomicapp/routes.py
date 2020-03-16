from flask import render_template
from genomicapp import app
from genomicapp.forms import QueryForm
from genomicapp.auto_query_other import run_auto_query
@app.route("/", methods=['POST', 'GET'])
def home():
	form = QueryForm()
	#need to validate submission

	if form.validate_on_submit():
		print(form.gsps.data)
		run_auto_query(form.antibiotic.data, form.organism.data,form.gspr.data,form.gsps.data)
	return render_template("home.html", title='Home', form=form)
