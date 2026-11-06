from flask import Blueprint, flash, redirect, render_template, request, url_for

from . import db
from .models import Todo

bp = Blueprint("todo", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            db.session.add(Todo(title=title))
            db.session.commit()
            flash("Задача добавлена")
        else:
            flash("Введите название задачи")
        return redirect(url_for("todo.index"))

    todos = Todo.query.order_by(Todo.id.desc()).all()
    return render_template("index.html", todos=todos)


@bp.route("/<int:todo_id>/edit", methods=["GET", "POST"])
def edit(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            todo.title = title
            db.session.commit()
            flash("Задача изменена")
        return redirect(url_for("todo.index"))
    return render_template("edit.html", todo=todo)


@bp.route("/<int:todo_id>/toggle")
def toggle(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("todo.index"))


@bp.route("/<int:todo_id>/delete")
def delete(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash("Задача удалена")
    return redirect(url_for("todo.index"))


@bp.app_errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404
