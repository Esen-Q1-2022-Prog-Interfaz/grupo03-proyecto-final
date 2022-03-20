from flask_sqlalchemy import SQLAlchemy
from app import app

from db.db import db

SQLAlchemy(app)

with app.app_context():
    db.create_all()

if "__main__" == __name__:
    app.run(debug=True)

