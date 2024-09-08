from flask import Flask
from flask_cors import CORS
from app.routes.owner_routes import owner_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(owner_routes)