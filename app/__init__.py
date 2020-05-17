from flask import Flask, redirect, render_template
from app.database import setup_db

app = Flask(__name__)
app.secret_key = 'skaldhskajl903'
app.debug = True

setup_db(app)

from . import routes, emails, models


