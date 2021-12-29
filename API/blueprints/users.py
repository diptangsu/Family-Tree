from flask import Blueprint, request
from flask_jwt import current_identity, jwt_required
from helpers.http.status_codes import Status

from helpers.http import Response
from managers.users import (
    create_user,
    get_user,
    get_user_children,
    get_user_grandparents,
    get_user_parents,
    get_user_siblings,
    update_user,
    delete_user,
)

USERS_BLUEPRINT = Blueprint('users', __name__)


@USERS_BLUEPRINT.route('', methods=['POST'])
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    phone = request.json.get('phone')
    address = request.json.get('address')
    dob = request.json.get('dob')

    response = create_user(email, password, first_name, last_name, phone, address, dob)
    return response


@USERS_BLUEPRINT.route('/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
@jwt_required()
def user_operations(user_id: int):
    if request.method in ('PATCH', 'DELETE') and current_identity.id != user_id:
        return Response.error('You are not authorized to perform this operation.', Status.UNAUTHORIZED)

    if request.method == 'GET':
        response = get_user(user_id)
        return response
    elif request.method == 'PATCH':
        response = update_user(**request.json)
        return response
    elif request.method == 'DELETE':
        response = delete_user(user_id)
        return response


@USERS_BLUEPRINT.route('/<int:user_id>/children', methods=['GET'])
@jwt_required()
def user_children(user_id: int):
    response = get_user_children(user_id)
    return response


@USERS_BLUEPRINT.route('/<int:user_id>/parents', methods=['GET'])
@jwt_required()
def user_parents(user_id: int):
    response = get_user_parents(user_id)
    return response


@USERS_BLUEPRINT.route('/<int:user_id>/siblings', methods=['GET'])
@jwt_required()
def user_siblings(user_id: int):
    response = get_user_siblings(user_id)
    return response


@USERS_BLUEPRINT.route('/<int:user_id>/grandparents', methods=['GET'])
@jwt_required()
def user_grandparents(user_id: int):
    response = get_user_grandparents(user_id)
    return response
