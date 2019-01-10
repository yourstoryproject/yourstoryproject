from app import db
from app.models.Tag import Tag
from flask import jsonify


def create_tag(name):
    if not Tag.query.filter_by(name=name).first():
        newTag = Tag(name=name)

        db.session.add(newTag)
        db.session.commit()

        response = {"message": "Successfully created tag", "status_code": 201}
    else:
        response = {"message": "Tag already exists", "status_code": 400}

    return response

def get_tag(id):
    tag = Tag.query.get(id)

    if not tag:
        response = {"error": "Tag not found", "status_code": 400}
    else:
        response = {"data": tag.to_json(), "status_code": 200}

    return response

def get_tags():
    tags = Tag.query.all()

    if len(tags) > 0:
        response = {"data": [tag.to_json() for tag in tags] , "status_code": 200}
    else:
        response = {"error": "No tags found", "status_code": 400}

    return response