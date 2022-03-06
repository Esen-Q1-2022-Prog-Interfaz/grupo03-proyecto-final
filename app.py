from flask import Flask
from routes.main.main import main

app = Flask(__name__)

app.register_blueprint(main)
