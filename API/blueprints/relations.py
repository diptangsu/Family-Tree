from flask import Blueprint, request
from managers.relations import create_parent, create_sibling, update_parent, delete_parent


RELATIONS_BLUEPRINT = Blueprint('relations', __name__)


@RELATIONS_BLUEPRINT.route('/parents', methods=['POST', 'PATCH', 'DELETE'])
def parent_ops():
    child_id = request.json.get('child_id')
    parent_id = request.json.get('parent_id')

    if request.method == 'POST':
        return create_parent(child_id, parent_id)
    elif request.method == 'PATCH':
        new_parent_id = request.json.get('new_parent_id')
        return update_parent(child_id, parent_id, new_parent_id)
    elif request.method == 'DELETE':
        return delete_parent(child_id, parent_id)


@RELATIONS_BLUEPRINT.route('/siblings', methods=['POST', 'PATCH', 'DELETE'])
def sibling_ops():
    user_id = request.json.get('user_id')
    sibling_id = request.json.get('sibling_id')

    if request.method == 'POST':
        return create_sibling(user_id, sibling_id)
    elif request.method == 'PATCH':
        new_sibling_id = request.json.get('new_sibling_id')
        return update_parent(user_id, sibling_id, new_sibling_id)
    elif request.method == 'DELETE':
        return delete_parent(user_id, sibling_id)
