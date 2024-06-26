from flask import Blueprint, jsonify, request
from app.models import Comment, db

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('/', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify([comment.to_dict() for comment in comments])


@bp.route('/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get_or_404(id)
    return jsonify(comment.to_dict())


@bp.route('/', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = Comment(**data)
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_comment(id):
    data = request.get_json()
    comment = Comment.query.get_or_404(id)
    for key, value in data.items():
        setattr(comment, key, value)
    db.session.commit()
    return jsonify(comment.to_dict())


@bp.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return '', 204
