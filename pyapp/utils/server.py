from flask import json, Response


def parse_response(res, status):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status
    )


def validate_entity(model, entity_id):
    """
    Check if <model> has a matching entity by <entity_id>
    """
    if entity_id is None:
        response = {"error": "Please provide entity_id"}

        return response

    if not model.query.filter_by(id=entity_id).first():
        response = {"error": "No entity found with entity_id: " + str(entity_id)}

        return response
    else:
        return None
