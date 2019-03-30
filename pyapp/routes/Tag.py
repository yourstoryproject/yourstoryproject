from flask import Blueprint, request
from pyapp.api.Tag import create_tag, edit_tag, get_tags

blueprint = Blueprint('tags', __name__, url_prefix='/api/v1/tags')


@blueprint.route('/', methods=['GET'])
@blueprint.route('/get_tags/', methods=['GET'])
def get_tags_route():
    tag_id = request.args.get('tag_id')

    response = get_tags(tag_id)

    return response


@blueprint.route('/create/', methods=['POST'])
def add_tag_route():
    tag_name = request.args.get('tag_name')

    response = create_tag(tag_name)

    return response


@blueprint.route('/edit/', methods=['PUT'])
def edit_tag_route():
    tag_id = request.args.get('tag_id')
    tag_name = request.args.get('tag_name')

    response = edit_tag(tag_id=tag_id, tag_name=tag_name)

    return response
