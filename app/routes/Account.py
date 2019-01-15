from app.utils.server import parse_response
from app.models.Account import Account
from app.api.Account import create_account, get_account, get_accounts
from flask import Blueprint, render_template, request


blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('api.html')

@blueprint.route('/get_accounts/')
def getAllAccounts():
    response = get_accounts()

    return render_template('api.html', response=response)

@blueprint.route('/get_account/', methods=['GET'])
def getSingleAccount():
    accountId = request.args.get('accountId')

    response = get_account(accountId)

    return render_template('api.html', response=response)

@blueprint.route('/create/', methods=['POST'])
def add_account(email, password):
    email = request.args.get('email')
    password = request.args.get('password')

    response = create_account(email, password)

    return parse_response(response, response["status_code"])