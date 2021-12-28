from flask import Blueprint, request

from managers.users import create_user, get_user, get_user_parents, get_user_siblings, get_user_grandparents, get_user_children

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


@USERS_BLUEPRINT.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def user_operations(id: int):
    if request.method == 'GET':
        response = get_user(id)
        return response
    elif request.method == 'PATCH':
        response = update_user(**request.json)
        return response
    elif request.method == 'DELETE':
        response = delete_user(id)
        return response


@USERS_BLUEPRINT.route('/<int:id>/children', methods=['GET'])
def user_children(id: int):
    response = get_user_children(id)
    return response


@USERS_BLUEPRINT.route('/<int:id>/parents', methods=['GET'])
def user_parents(id: int):
    response = get_user_parents(id)
    return response


@USERS_BLUEPRINT.route('/<int:id>/siblings', methods=['GET'])
def user_siblings(id: int):
    response = get_user_siblings(id)
    return response


@USERS_BLUEPRINT.route('/<int:id>/grandparents', methods=['GET'])
def user_grandparents(id: int):
    response = get_user_grandparents(id)
    return response
