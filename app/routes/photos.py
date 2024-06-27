from flask import Blueprint, jsonify, request
from app.models import Photo, db

bp = Blueprint('photos', __name__, url_prefix='/photos')


@bp.route('/', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_dict() for photo in photos])


@bp.route('/<int:id>', methods=['GET'])
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    return jsonify(photo.to_dict())


@bp.route('/', methods=['POST'])
def create_photo():
    data = request.get_json()
    photo = Photo(**data)
    db.session.add(photo)
    db.session.commit()
    return jsonify(photo.to_dict()), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_photo(id):
    data = request.get_json()
    photo = Photo.query.get_or_404(id)
    for key, value in data.items():
        setattr(photo, key, value)
    db.session.commit()
    return jsonify(photo.to_dict())


@bp.route('/<int:id>', methods=['DELETE'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    return '', 204
