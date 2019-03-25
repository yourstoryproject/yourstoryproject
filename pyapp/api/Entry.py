from pyapp import db
from pyapp.models.Entry import Entry
from pyapp.utils.server import parse_response, validate_entity


def get_entries(entryId):
    try:
        if entryId is None:
            entries = Entry.query.all()
        else:
            response = {"entries": validate_entity(
                model=Entry, entityId=entryId)}

            if response:
                return parse_response(response, 400)

            entries = Entry.query.get(entryId)

        response = {"entries": [entry.to_json() for entry in entries]}

        return parse_response(response, 200)

    except BaseException as e:
        response = {"entries": {
            "error": "Unable to get entries", "message": str(e)}}

        return parse_response(response, 400)
