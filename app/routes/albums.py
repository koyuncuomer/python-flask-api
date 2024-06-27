from flask import Blueprint, jsonify, request
from app.models import Album, db

bp = Blueprint('albums', __name__, url_prefix='/albums')


@bp.route('/', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    return jsonify([album.to_dict() for album in albums])


@bp.route('/<int:id>', methods=['GET'])
def get_album(id):
    album = Album.query.get_or_404(id)
    return jsonify(album.to_dict())


@bp.route('/', methods=['POST'])
def create_album():
    data = request.get_json()
    album = Album(**data)
    db.session.add(album)
    db.session.commit()
    return jsonify(album.to_dict()), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_album(id):
    data = request.get_json()
    album = Album.query.get_or_404(id)
    for key, value in data.items():
        setattr(album, key, value)
    db.session.commit()
    return jsonify(album.to_dict())


@bp.route('/<int:id>', methods=['DELETE'])
def delete_album(id):
    album = Album.query.get_or_404(id)
    db.session.delete(album)
    db.session.commit()
    return '', 204
