from flask import Blueprint, jsonify, request
from app.models import Todo, db

bp = Blueprint('todos', __name__, url_prefix='/todos')


@bp.route('/', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])


@bp.route('/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo.to_dict())


@bp.route('/', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = Todo(**data)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    todo = Todo.query.get_or_404(id)
    for key, value in data.items():
        setattr(todo, key, value)
    db.session.commit()
    return jsonify(todo.to_dict())


@bp.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204
