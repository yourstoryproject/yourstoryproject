from pyapp.utils.server import parse_response
from pyapp.models import Entry
from pyapp.api.Entry import get_entries
from flask import Blueprint, render_template, request

blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')


@blueprint.route('/', methods=['GET'])
@blueprint.route('/get_entries/', methods=['GET'])
def getEntries():
    entryId = request.args.get('entryId')

    response = get_entries(entryId)

    return response
