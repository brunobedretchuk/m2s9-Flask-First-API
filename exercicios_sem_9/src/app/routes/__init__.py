from src.app.controllers.technologies import technology

def routes(app):
  app.register_blueprint(technology)
