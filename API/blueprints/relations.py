from flask import Blueprint, request
from flask_jwt import current_identity, jwt_required
from helpers.http.status_codes import Status

from helpers.http import Response
from managers.relations import (
    create_parent,
    create_sibling,
    delete_parent,
    update_parent,
    update_sibling,
    delete_sibling,
)

RELATIONS_BLUEPRINT = Blueprint('relations', __name__)


@RELATIONS_BLUEPRINT.route('/parents', methods=['POST', 'PATCH', 'DELETE'])
@jwt_required()
def parent_ops():
    child_id = request.json.get('child_id')
    parent_id = request.json.get('parent_id')

    if request.method in ('PATCH', 'DELETE') and current_identity.id != child_id:
        return Response.error('You are not authorized to perform this operation.', Status.UNAUTHORIZED)

    if request.method == 'POST':
        return create_parent(child_id, parent_id)
    elif request.method == 'PATCH':
        new_parent_id = request.json.get('new_parent_id')
        return update_parent(child_id, parent_id, new_parent_id)
    elif request.method == 'DELETE':
        return delete_parent(child_id, parent_id)


@RELATIONS_BLUEPRINT.route('/siblings', methods=['POST', 'PATCH', 'DELETE'])
@jwt_required()
def sibling_ops():
    user_id = request.json.get('user_id')
    sibling_id = request.json.get('sibling_id')

    if request.method in ('PATCH', 'DELETE') and current_identity.id != user_id:
        return Response.error('You are not authorized to perform this operation.', Status.UNAUTHORIZED)

    if request.method == 'POST':
        return create_sibling(user_id, sibling_id)
    elif request.method == 'PATCH':
        new_sibling_id = request.json.get('new_sibling_id')
        return update_sibling(user_id, sibling_id, new_sibling_id)
    elif request.method == 'DELETE':
        return delete_sibling(user_id, sibling_id)
