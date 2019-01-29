from pyapp.utils.server import parse_response
from pyapp.models.Account import Account
from pyapp.api.Account import create_account, edit_account, get_account, get_accounts
from flask import Blueprint, render_template, request


blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')


@blueprint.route('/get_accounts/')
def getAllAccounts():
    response = get_accounts()

    return parse_response(response, response["status"])


@blueprint.route('/get_account/', methods=['GET'])
def getSingleAccount():
    accountId = request.args.get('accountId')

    response = get_account(accountId)

    return parse_response(response, response["status"])


@blueprint.route('/create/', methods=['POST'])
def add_account():
    email = request.args.get('email')
    password = request.args.get('password')

    response = create_account(email, password)

    return parse_response(response, response["status"])


@blueprint.route('/edit/', methods=['PUT'])
def editAccount():
    accountId = request.args.get('accountId')
    email = request.args.get('email')
    password = request.args.get('password')

    response = edit_account(
        accountId=accountId,
        email=email,
        password=password)

    return parse_response(response, response["status"])
