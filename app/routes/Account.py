from app.utils.server import parse_response
from app.models.Account import Account
from app.api.Account import get_account, get_accounts
from flask import Blueprint


blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')

@blueprint.route('/', methods=['GET'])
def accounts():
    response = get_accounts()

    return parse_response(response, 200)

@blueprint.route('/<int:accountId>', methods=['GET'])
def account(accountId):
    response = get_account(accountId)

    return parse_response(response, 200)