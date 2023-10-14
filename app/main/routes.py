# это контроллер вручную прописываем юрд и объекты

from flask import render_template  # отвечает за визуализацию шаблона
from app.main import bp


@bp.route('/')
def index():
    return render_template("index.html")
