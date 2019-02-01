from flask import json, Response


def parse_response(res, status):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps({"data": res}),
        status=status
    )


def validate_entity(model, entityId):
    """
    Check if <model> has a matching entity by <entityId>
    """
    if entityId == None:
        response = {"error": "Please provide entityId"}

        return response

    if not model.query.filter_by(id=entityId).first():
        response = {"error": "No entity found with entityId: " + entityId}

        return response
    else:
        return None
