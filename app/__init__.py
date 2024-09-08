from flask import Flask
from flask_cors import CORS
from app.routes.owner_routes import owner_routes
from app.database import engine, Base

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Create database tables
    Base.metadata.create_all(bind=engine)

    app.register_blueprint(owner_routes)

    return app