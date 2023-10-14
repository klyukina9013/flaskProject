from flask import Blueprint  # систему делим на несколько частей

bp = Blueprint('main', __name__)  # эйм позволяет найти корневую папку приложения

from app.main import routes
