from flask import Blueprint, jsonify, request
from app.models import Post, Comment, db

bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])


@bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict())


@bp.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    post = Post(**data)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    post = Post.query.get_or_404(id)
    for key, value in data.items():
        setattr(post, key, value)
    db.session.commit()
    return jsonify(post.to_dict())


@bp.route('/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return '', 204


@bp.route('/<int:post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([comment.to_dict() for comment in comments])