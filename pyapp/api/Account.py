from pyapp import db
from pyapp.models.Account import Account
from pyapp.utils.server import parse_response, validate_entity
from bleach.sanitizer import Cleaner

cleaner = Cleaner()


def create_account(email, password):
    email = cleaner.clean(email)
    password = cleaner.clean(password)

    if not Account.query.filter_by(email=email).first():
        try:
            newAccount = Account(email=email, password=password)

            db.session.add(newAccount)
            db.session.commit()

            response = {"accounts": {
                "message": "Successfully created account"}}

            return parse_response(response, 201)
        except BaseException as e:
            response = {"accounts": {
                "error": "Unable to create account", "message": str(e)}}

            return parse_response(response, 400)
    else:
        response = {"accounts": {"message": "Email already exists"}}

        return parse_response(response, 400)


def edit_account(account_id, email, password):
    account_id = int(account_id)
    email = cleaner.clean(email)
    password = cleaner.clean(password)

    response = {"accounts": validate_entity(model=Account, entityId=account_id)}

    if response:
        return parse_response(response, 400)

    try:
        account = Account.query.get(account_id)

        if email != '':
            account.email = email

        db.session.commit()

        response = {"accounts": {"success": "Successfully changed email."}}

        return parse_response(response, 200)
    except BaseException as e:
        response = {"accounts": {"error": "Unable to update information: " + e}}

        return parse_response(response, 500)


def get_accounts(account_id):
    try:
        if account_id is None:
            accounts = Account.query.all()
        else:
            account_id = int(account_id)

            response = {"accounts": validate_entity(
                model=Account, entityId=account_id)}

            if response:
                return parse_response(response, 400)

            accounts = Account.query.get(account_id)

        response = {"accounts": [account.to_json() for account in accounts]}

        return parse_response(response, 200)
    except BaseException:
        response = {"accounts": {
            "error": "Unable to perform query, please check parameters and try again"}}

        return parse_response(response, 500)
