from pyapp import db
from pyapp.models.Tag import Tag
from pyapp.utils.server import parse_response, validate_entity
from bleach.sanitizer import Cleaner
import datetime

cleaner = Cleaner()


def create_tag(name):
    name = cleaner.clean(name)

    if not Tag.query.filter_by(name=name).first():
        new_tag = Tag(name=name)

        db.session.add(new_tag)
        db.session.commit()

        response = {"tags": {"message": "Successfully created tag"}}

        return parse_response(response, 201)
    else:
        response = {"tags": {"message": "Tag already exists"}}

        return parse_response(response, 400)


def edit_tag(tag_id, tag_name):
    tag_id = int(tag_id)
    tag_name = cleaner.clean(tag_name)

    if tag_id == '':
        response = {"tags": {"error": "Please provide an tag Id"}}

        return parse_response(response, 400)

    if not Tag.query.filter_by(id=tag_id).first():
        response = {"tags": {"error": "Tag does not exist"}}

        return parse_response(response, 400)

    if tag_name == '':
        response = {"tags": {"error": "Please provide new tag name"}}

        return parse_response(response, 400)

    try:
        tag = Tag.query.get(tag_id)

        oldTag = tag.name

        tag.modified_on = datetime.datetime.utcnow()
        tag.name = tag_name

        db.session.commit()

        response = {"tags": {"success": "Tag name was changed from " +
                                        oldTag + " to " + tag_name}}

        return parse_response(response, 201)
    except BaseException:
        response = {"tags": {"error": "Unable to change tag name."}}

        return parse_response(response, 500)


def get_tags(tag_id):
    tag_id = int(tag_id)

    try:
        if tag_id is None:
            tags = Tag.query.all()
        else:
            response = {"tags": validate_entity(model=Tag, entityId=tag_id)}

            if response:
                return parse_response(response, 400)

            tags = Tag.query.get(tag_id)

        response = {"tags": [tag.to_json() for tag in tags]}

        return parse_response(response, 200)

    except BaseException as e:
        response = {"tags": {"error": "Unable to get tags", "message": str(e)}}

        return parse_response(response, 400)
