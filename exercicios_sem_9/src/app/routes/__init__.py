from flask import Flask
from src.app.controllers.users import user

def routes(app):
  app.register_blueprint(user)
