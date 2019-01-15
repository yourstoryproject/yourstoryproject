from app import db
from app.models.Account import Account


def create_account(email, password):
    if not Account.query.filter_by(email=email).first():
        newAccount = Account(email=email, password=password)

        db.session.add(newAccount)
        db.session.commit()

        response = {"message": "Successfully created account", "status_code": 201}
    else:
        response = {"message": "Email already exists", "status_code": 400}

    return response

def get_account(accountId):
    if accountId == '':
        response = {"error": "Please provide an account Id", "status_code": 400}

        return response

    try:
        account = Account.query.get(accountId)

        if not account:
            response = {"error": "Account not found", "status_code": 400}
        else:
            response = {"data": [account.to_json()], "status_code": 200}

        return response
    except:
        response = {"error": "Unable to perform query, please check parameters and try again", "status_code": 500}

        return response


def get_accounts():
    accounts = Account.query.all()

    if len(accounts) > 0:
        response = {"data": [account.to_json() for account in accounts] , "status_code": 200}
    else:
        response = {"error": "No accounts found", "status_code": 400}

    return response