
from flask import Flask
from routes.main.main import main
from routes.admin.admin import admin

app = Flask(__name__)
app.config.from_object("config.BaseConfig")

app.register_blueprint(admin)
app.register_blueprint(main)
