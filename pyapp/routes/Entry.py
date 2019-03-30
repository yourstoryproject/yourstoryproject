from flask import Blueprint, request
from pyapp.api.Entry import get_entries

blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')


@blueprint.route('/', methods=['GET'])
@blueprint.route('/get_entries/', methods=['GET'])
def get_entries_route():
    entry_id = request.args.get('entry_id')

    response = get_entries(entry_id)

    return response
