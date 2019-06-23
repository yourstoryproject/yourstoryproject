from flask import Blueprint, render_template, request
from flask_login import login_required
from pyapp.api.Account import create_account, edit_account, get_accounts
from pyapp.utils.auth import role_required
from pyapp.utils.constants import ROLES

blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')


@blueprint.route('/', methods=['GET'])
@blueprint.route('/get_accounts/', methods=['GET'])
@login_required
@role_required(ROLES.ADMIN)
def get_accounts_route():
    account_id = request.args.get('account_id')

    response = get_accounts(account_id)

    return response


@blueprint.route('/create/', methods=['POST'])
def add_account_route():
    email = request.args.get('email')
    password = request.args.get('password')

    response = create_account(email, password)

    return response


@blueprint.route('/edit/', methods=['PUT'])
@login_required
def edit_account_route():
    account_id = request.args.get('account_id')
    email = request.args.get('email')
    password = request.args.get('password')

    response = edit_account(
        account_id=account_id,
        email=email,
        password=password)

    return response
