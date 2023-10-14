from flask import render_template  # отвечает за визуализацию шаблона
from app.page import bp


@bp.route('/')
def index():
    return render_template("page/index.html")
