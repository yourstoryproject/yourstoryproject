from pyapp import db
from pyapp.models.Tag import Tag
import datetime


def create_tag(name):
    if not Tag.query.filter_by(name=name).first():
        newTag = Tag(name=name)

        db.session.add(newTag)
        db.session.commit()

        response = {"message": "Successfully created tag", "status": 201}
    else:
        response = {"message": "Tag already exists", "status": 400}

    return response


def edit_tag(tagId, tagName):
    if tagId == '':
        response = {"error": "Please provide an tag Id", "status": 400}

        return response

    if not Tag.query.filter_by(id=tagId).first():
        response = {"error": "Tag does not exist", "status": 400}

        return response

    if tagName == '':
        response = {"error": "Please provide new tag name", "status": 400}

        return response

    try:
        tag = Tag.query.get(tagId)

        oldTag = tag.name

        tag.modified_on = datetime.datetime.utcnow()
        tag.name = tagName

        db.session.commit()

        response = {"success": "Tag name was changed from " +
                    oldTag + " to " + tagName, "status": 201}

        return response
    except BaseException:
        response = {"error": "Unable to change tag name.", "status": 500}

        return response


def get_tag(tagId):
    if tagId == '':
        response = {"error": "Please provide an tag Id", "status": 400}

        return response

    try:
        tag = Tag.query.get(tagId)

        if not tag:
            response = {"error": "Tag not found", "status": 400}
        else:
            response = {"data": [tag.to_json()], "status": 200}

        return response
    except BaseException:
        response = {
            "error": "Unable to perform query, please check parameters and try again",
            "status": 500}

        return response


def get_tags():
    tags = Tag.query.all()

    if len(tags) > 0:
        response = {
            "data": [
                tag.to_json() for tag in tags],
            "status": 200}
    else:
        response = {"error": "No tags found", "status": 400}

    return response
