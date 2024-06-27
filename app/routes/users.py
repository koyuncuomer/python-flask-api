from flask import Blueprint, jsonify, request
from app.models import User, Post, Album, Todo, db

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@bp.route('/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id=user_id).all()
    return jsonify([post.to_dict() for post in posts])


@bp.route('/<int:user_id>/albums', methods=['GET'])
def get_user_albums(user_id):
    user = User.query.get_or_404(user_id)
    albums = Album.query.filter_by(user_id=user_id).all()
    return jsonify([album.to_dict() for album in albums])


@bp.route('/<int:user_id>/todos', methods=['GET'])
def get_user_todos(user_id):
    user = User.query.get_or_404(user_id)
    todos = Todo.query.filter_by(user_id=user_id).all()
    return jsonify([todo.to_dict() for todo in todos])
