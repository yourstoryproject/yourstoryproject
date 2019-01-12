from app import db
from app.models.Account import Account


def get_account(id):
    account = Account.query.get(id)

    if not account:
        response = {"error": "Account not found", "status_code": 400}
    else:
        response = {"data": account.to_json(), "status_code": 200}

    return response

def get_accounts():
    accounts = Account.query.all()

    if len(accounts) > 0:
        response = {"data": [account.to_json() for account in accounts] , "status_code": 200}
    else:
        response = {"error": "No accounts found", "status_code": 400}

    return response