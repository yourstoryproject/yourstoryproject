from app import db
from app.models.Tag import Tag
import datetime


def create_tag(name):
    if not Tag.query.filter_by(name=name).first():
        newTag = Tag(name=name)

        db.session.add(newTag)
        db.session.commit()

        response = {"message": "Successfully created tag", "status_code": 201}
    else:
        response = {"message": "Tag already exists", "status_code": 400}

    return response

def edit_tag(tagId, tagName):
    if tagId == '':
        response = {"error": "Please provide an tag Id", "status_code": 400}

        return response

    if not Tag.query.filter_by(id=tagId).first():
        response = {"error": "Tag does not exist", "status_code": 400}

        return response

    if tagName == '':
        response = {"error": "Please provide new tag name", "status_code": 400}

        return response

    try:
        tag = Tag.query.get(tagId)

        oldTag = tag.name

        tag.modified_on = datetime.datetime.utcnow()
        tag.name = tagName

        db.session.commit()

        response = {"success": "Tag name was changed from " + oldTag + " to " + tagName, "status_code": 201}

        return response
    except:
        response = {"error": "Unable to change tag name.", "status_code": 500}

        return response

def get_tag(tagId):
    if tagId == '':
        response = {"error": "Please provide an tag Id", "status_code": 400}

        return response

    try:
        tag = Tag.query.get(tagId)

        if not tag:
            response = {"error": "Tag not found", "status_code": 400}
        else:
            response = {"data": [tag.to_json()], "status_code": 200}

        return response
    except:
        response = {"error": "Unable to perform query, please check parameters and try again", "status_code": 500}

        return response

def get_tags():
    tags = Tag.query.all()

    if len(tags) > 0:
        response = {"data": [tag.to_json() for tag in tags] , "status_code": 200}
    else:
        response = {"error": "No tags found", "status_code": 400}

    return response