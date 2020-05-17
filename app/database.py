from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


database_name = 'isellubuy'
database_path = 'mysql://root:@localhost/remindme'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()