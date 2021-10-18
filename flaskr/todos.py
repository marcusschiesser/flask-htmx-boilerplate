from flask import Blueprint, render_template, request, current_app as app

bp = Blueprint('todos', __name__, url_prefix='/todos')

todos = [{'id': 1, 'name': 'Clean room'}]

@bp.route("/", methods=["GET"])
def get_todos():
    return render_template("bp/todos/todos.html", todos=todos)

@bp.route("/add", methods=["POST"])
def add_todo():
    todo_name = request.form.get("todo")
    id = len(todos)+1

    todos.append({'id': id, 'name': todo_name})

    return render_template("bp/todos/todos.html", todos=todos)


