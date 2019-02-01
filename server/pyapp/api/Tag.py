from pyapp import db
from pyapp.models.Tag import Tag
from pyapp.utils.server import parse_response, validate_entity
import datetime


def create_tag(name):
    if not Tag.query.filter_by(name=name).first():
        newTag = Tag(name=name)

        db.session.add(newTag)
        db.session.commit()

        response = {"tags": {"message": "Successfully created tag"}}

        return parse_response(response, 201)
    else:
        response = {"tags": {"message": "Tag already exists"}}

        return parse_response(response, 400)


def edit_tag(tagId, tagName):
    if tagId == '':
        response = {"tags": {"error": "Please provide an tag Id"}}

        return parse_response(response, 400)

    if not Tag.query.filter_by(id=tagId).first():
        response = {"tags": {"error": "Tag does not exist"}}

        return parse_response(response, 400)

    if tagName == '':
        response = {"tags": {"error": "Please provide new tag name"}}

        return parse_response(response, 400)

    try:
        tag = Tag.query.get(tagId)

        oldTag = tag.name

        tag.modified_on = datetime.datetime.utcnow()
        tag.name = tagName

        db.session.commit()

        response = {"tags": {"success": "Tag name was changed from " +
                             oldTag + " to " + tagName}}

        return parse_response(response, 201)
    except BaseException:
        response = {"tags": {"error": "Unable to change tag name."}}

        return parse_response(response, 500)


def get_tags(tagId):
    try:
        if tagId == None:
            tags = Tag.query.all()
        else:
            response = {"tags": validate_entity(model=Tag, entityId=tagId)}

            if response:
                return parse_response(response, 400)

            tags = Tag.query.get(tagId)

        response = {"tags": [tag.to_json() for tag in tags]}

        return parse_response(response, 200)

    except BaseException as e:
        response = {"tags": {"error": "Unable to get tags", "message": str(e)}}

        return parse_response(response, 400)
