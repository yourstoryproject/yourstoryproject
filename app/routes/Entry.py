from app.utils.server import parse_response
from app.models import Entry
from app.api.Entry import get_entry, get_entries
from flask import Blueprint, jsonify, render_template, request


blueprint = Blueprint('entries', __name__, url_prefix='/api/v1/entries')

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')

@blueprint.route('/get_entries/', methods=['GET'])
def getAllEntries():
    response = get_entries()

    return render_template('api.html', response=response)

@blueprint.route('/get_entry/', methods=['GET'])
def getSingleEntry():
    entryId = request.args.get('entryId')

    response = get_entry(entryId)

    return render_template('api.html', response=response)
