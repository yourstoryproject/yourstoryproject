from app.utils.server import parse_response
from app.models.Account import Account
from flask import Blueprint


blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')

@blueprint.route('/', methods=['GET'])
def accounts():
    accounts = Account.get_accounts()

    response = {'accounts': [account.to_json() for account in accounts]}

    return parse_response(response, 200)


@blueprint.route('/<int:accountId>', methods=['GET'])
def account(accountId):
    account = Account.get_account(accountId)

    if not account:
        return parse_response({'error': 'Account not found'}, 404)

    response = {'account': account.to_json()}

    return parse_response(response, 200)