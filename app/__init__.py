from flask import Flask
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    register_routes(app)
    return app