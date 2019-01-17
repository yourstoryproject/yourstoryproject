from pyapp import db
from pyapp.models.Account import Account
from pyapp.utils.server import validate_entity


def create_account(email, password):
    if not Account.query.filter_by(email=email).first():
        newAccount = Account(email=email, password=password)

        db.session.add(newAccount)
        db.session.commit()

        response = {
            "message": "Successfully created account",
            "status": 201}
    else:
        response = {"message": "Email already exists", "status": 400}

    return response


def edit_account(accountId, email, password):
    response = validate_entity(model=Account, entityId=accountId)

    if response:
        return response

    try:
        account = Account.query.get(accountId)

        if email != '':
            oldEmail = account.email
            account.email = email

        db.session.commit()

        response = {
            "success": "Successfully changed email from " +
            oldEmail +
            " to " +
            email,
            "status": 200}

        return response
    except BaseException:
        response = {
            "error": "Unable to update information",
            "status": 500}

        return response


# Email should already be validated at this point
# This api should assume user is also authenticated?


def get_account(accountId):
    response = validate_entity(model=Account, entityId=accountId)

    if response:
        return response

    try:
        account = Account.query.get(accountId)

        if not account:
            response = {"error": "Account not found", "status": 400}
        else:
            response = {"data": [account.to_json()], "status": 200}

        return response
    except BaseException:
        response = {
            "error": "Unable to perform query, please check parameters and try again",
            "status": 500}

        return response


def get_accounts():
    accounts = Account.query.all()

    if len(accounts) > 0:
        response = {
            "data": [
                account.to_json() for account in accounts],
            "status": 200}
    else:
        response = {"error": "No accounts found", "status": 400}

    return response
