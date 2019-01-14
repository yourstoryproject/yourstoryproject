from app import db
from app.models.Entry import Entry


def get_entry(entryId):
    if entryId == '':
        response = {"error": "Please provide an entry Id", "status_code": 400}

        return response

    entry = Entry.query.get(entryId)

    if not entry:
        response = {"error": "Entry not found", "status_code": 400}
    else:
        response = {"data": [entry.to_json()], "status_code": 200}

    return response

def get_entries():
    entries = Entry.query.all()

    if len(entries) > 0:
        response = {"data": [entry.to_json() for entry in entries] , "status_code": 200}
    else:
        response = {"error": "No entries found", "status_code": 400}

    return response