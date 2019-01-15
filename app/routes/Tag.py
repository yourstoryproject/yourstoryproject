from app.utils.server import parse_response
from app.models import Tag
from app.api.Tag import create_tag, get_tag, get_tags
from flask import Blueprint, jsonify, render_template, request


blueprint = Blueprint('tags', __name__, url_prefix='/api/v1/tags')

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')

@blueprint.route('/get_tags/')
def getAllTags():
    response = get_tags()

    return render_template('api.html', response=response)

@blueprint.route('/get_tag/', methods=['GET'])
def getSingleTag():
    tagId = request.args.get('tagId')

    response = get_tag(tagId)

    return render_template('api.html', response=response)

@blueprint.route('/create/<string:tagName>', methods=['POST'])
def add_tag(tagName):
    response = create_tag(tagName)

    return parse_response(response, response["status_code"])