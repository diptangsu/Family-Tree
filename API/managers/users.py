from datetime import datetime
from database.models import User
from helpers.decorators import res_err_handler
from helpers.http import Response, Status


@res_err_handler
def create_user(
    email: str,
    password: str,
    first_name: str,
    last_name: str,
    phone: str,
    address: str,
    dob: str,
) -> Response:
    """Create a user in the DB.

    Args:
        name (str): The name of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        phone (str): The phone number of the user.
        address (str): The address of the user.
        dob (str): The date of birth of the user.

    Returns:
        Response: Id of the created user.
    """
    dob = datetime.strptime(dob, '%Y-%m-%d')
    user = User.create(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address,
        dob=dob,
    )

    return Response.success({'user_id': user.id}, Status.CREATED)


@res_err_handler
def update_user(
    user_id: int,
    email: str = None,
    password: str = None,
    first_name: str = None,
    last_name: str = None,
    phone: str = None,
    address: str = None,
    dob: str = None,
) -> Response:
    """Update a user in the DB.

    Args:
        user_id (int): The id of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        phone (str): The phone number of the user.
        address (str): The address of the user.
        dob (str): The date of birth of the user.

    Returns:
        Response: Details of the updated user.
    """
    update_kwargs = {}
    if email:
        update_kwargs['email'] = email
    if password:
        update_kwargs['password'] = password
    if first_name:
        update_kwargs['first_name'] = first_name
    if last_name:
        update_kwargs['last_name'] = last_name
    if phone:
        update_kwargs['phone'] = phone
    if address:
        update_kwargs['address'] = address
    if dob:
        update_kwargs['dob'] = datetime.strptime(dob, '%Y-%m-%d')

    user = User.get(user_id)
    user.update(**update_kwargs)

    return Response.success({'user': user.to_dict()}, Status.OK)


@res_err_handler
def delete_user(user_id: int) -> Response:
    """Delete a user in the DB.

    Args:
        user_id (int): The id of the user.

    Returns:
        Response: Details of the deleted user.
    """
    user = User.get(user_id)
    user_data = user.to_dict()
    user.delete()

    return Response.success(
        {'deleted_user': user_data, 'message': 'User deleted.'}, Status.OK
    )


@res_err_handler
def get_user(user_id: int) -> Response:
    """Get a user from the DB.

    Args:
        user_id (int): The id of the user.

    Returns:
        Response: The user.
    """
    user = User.get(user_id)
    return Response.success({'user': user.to_dict()})


@res_err_handler
def get_user_parents(user_id: int) -> Response:
    """Get the parents of a user from the DB.

    Args:
        user_id (int): The id of the user.

    Returns:
        Response: The parents of the user.
    """
    user = User.get(user_id)
    parents = [parent.to_dict() for parent in user.parents()]

    return Response.success({'parents': parents})


@res_err_handler
def get_user_grandparents(user_id: int) -> Response:
    """Get the grandparents of a user from the DB.

    Args:
        user_id (int): The id of the user.

    Returns:
        Response: The grandparents of the user.
    """
    user = User.get(user_id)
    grandparents = [grandparent.to_dict() for grandparent in user.grandparents()]

    return Response.success({'grandparents': grandparents})


@res_err_handler
def get_user_siblings(user_id: int) -> Response:
    """Get the siblings of a user from the DB.

    Args:
        user_id (int): The id of the user.

    Returns:
        Response: The siblings of the user.
    """
    user = User.get(user_id)
    siblings = [sibling.to_dict() for sibling in user.siblings()]

    return Response.success({'siblings': siblings})


@res_err_handler
def get_user_children(user_id: int) -> Response:
    """Get the children of a user from the DB.

    Args:
        user_id (int): The id of the user.

    Returns:
        Response: The children of the user.
    """
    user = User.get(user_id)
    children = [child.to_dict() for child in user.children_recursive()]

    return Response.success({'children': children})
