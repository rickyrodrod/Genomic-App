from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '637f067193032e0cc80262555b624e0c'

from genomicapp import routes
