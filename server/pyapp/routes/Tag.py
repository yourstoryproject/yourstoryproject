from pyapp.utils.server import parse_response
from pyapp.models import Tag
from pyapp.api.Tag import create_tag, edit_tag, get_tag, get_tags
from flask import Blueprint, render_template, request


blueprint = Blueprint('tags', __name__, url_prefix='/api/v1/tags')


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')


@blueprint.route('/get_tags/')
def getAllTags():
    response = get_tags()

    return parse_response(response, response["status"])


@blueprint.route('/get_tag/', methods=['GET'])
def getSingleTag():
    tagId = request.args.get('tagId')

    response = get_tag(tagId)

    return parse_response(response, response["status"])


@blueprint.route('/create/', methods=['POST'])
def add_tag():
    tagName = request.args.get('tagName')

    response = create_tag(tagName)

    return parse_response(response, response["status"])


@blueprint.route('/edit/', methods=['PUT'])
def editTag():
    tagId = request.args.get('tagId')
    tagName = request.args.get('tagName')

    response = edit_tag(tagId=tagId, tagName=tagName)

    return parse_response(response, response["status"])
