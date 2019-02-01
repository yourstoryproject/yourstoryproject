from pyapp.utils.server import parse_response
from pyapp.models import Tag
from pyapp.api.Tag import create_tag, edit_tag, get_tags
from flask import Blueprint, render_template, request


blueprint = Blueprint('tags', __name__, url_prefix='/api/v1/tags')


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')


@blueprint.route('/get_tags/', methods=['GET'])
def tags():
    tagId = request.args.get('tagId')

    response = get_tags(tagId)

    return response


@blueprint.route('/create/', methods=['POST'])
def add_tag():
    tagName = request.args.get('tagName')

    response = create_tag(tagName)

    return response


@blueprint.route('/edit/', methods=['PUT'])
def editTag():
    tagId = request.args.get('tagId')
    tagName = request.args.get('tagName')

    response = edit_tag(tagId=tagId, tagName=tagName)

    return response
