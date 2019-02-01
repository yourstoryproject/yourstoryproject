from pyapp import db
from pyapp.models.Account import Account
from pyapp.utils.server import parse_response, validate_entity


def create_account(email, password):
    if not Account.query.filter_by(email=email).first():
        newAccount = Account(email=email, password=password)

        db.session.add(newAccount)
        db.session.commit()

        response = {"accounts": {"message": "Successfully created account"}}

        return parse_response(response, 201)
    else:
        response = {"accounts": {"message": "Email already exists"}}

    return parse_response(response, 400)


def edit_account(accountId, email, password):
    response = {"accounts": validate_entity(model=Account, entityId=accountId)}

    if response:
        return parse_response(response, 400)

    try:
        account = Account.query.get(accountId)

        if email != '':
            oldEmail = account.email
            account.email = email

        db.session.commit()

        response = {"accounts": {"success": "Successfully changed email from " +
                                 oldEmail +
                                 " to " +
                                 email}}

        return parse_response(response, 200)
    except BaseException:
        response = {"accounts": {"error": "Unable to update information"}}

        return parse_response(response, 500)


# Email should already be validated at this point
# This api should assume user is also authenticated?


def get_accounts(accountId):
    try:
        if accountId == None:
            accounts = Account.query.all()
        else:
            response = {"accounts": validate_entity(
                model=Account, entityId=accountId)}

            if response:
                return parse_response(response, 400)

            accounts = Account.query.get(accountId)

        response = {"accounts": [account.to_json() for account in accounts]}

        return parse_response(response, 200)
    except BaseException:
        response = {"accounts": {
            "error": "Unable to perform query, please check parameters and try again"}}

        return parse_response(response, 500)
