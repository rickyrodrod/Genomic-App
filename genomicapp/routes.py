from flask import render_template
from genomicapp import app

@app.route("/")
def home():
    return render_template("home.html")
