from pyapp.utils.server import parse_response
from pyapp.models import Entry
from pyapp.api.Entry import get_entry, get_entries
from flask import Blueprint, render_template, request


blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')


@blueprint.route('/get_entries/', methods=['GET'])
def getAllEntries():
    response = get_entries()

    return parse_response(response, response["status"])


@blueprint.route('/get_entry/', methods=['GET'])
def getSingleEntry():
    entryId = request.args.get('entryId')

    response = get_entry(entryId)

    return parse_response(response, response["status"])
