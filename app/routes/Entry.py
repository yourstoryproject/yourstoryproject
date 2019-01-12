from app.utils.server import parse_response
from app.models import Entry
from app.api.Entry import get_entry, get_entries
from flask import Blueprint, jsonify


blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')

@blueprint.route('/', methods=['GET'])
def entries():
    response = get_entries()

    return parse_response(response, response["status_code"])

@blueprint.route('/<int:entryId>', methods=['GET'])
def entry(entryId):
    response = get_entry(entryId)

    return parse_response(response, response["status_code"])
