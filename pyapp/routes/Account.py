from pyapp.utils.server import parse_response
from pyapp.models.Account import Account
from pyapp.api.Account import create_account, edit_account, get_accounts
from flask import Blueprint, render_template, request
from flask_login import login_required
from pyapp.utils.auth import role_required


blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')


@blueprint.route('/', methods=['GET'])
@blueprint.route('/get_accounts/', methods=['GET'])
@login_required
@role_required('admin')
def getAccounts():
    accountId = request.args.get('accountId')

    response = get_accounts(accountId)

    return response


@blueprint.route('/create/', methods=['POST'])
def add_account():
    email = request.args.get('email')
    password = request.args.get('password')

    response = create_account(email, password)

    return response


@blueprint.route('/edit/', methods=['PUT'])
@login_required
def editAccount():
    accountId = request.args.get('accountId')
    email = request.args.get('email')
    password = request.args.get('password')

    response = edit_account(
        accountId=accountId,
        email=email,
        password=password)

    return response
