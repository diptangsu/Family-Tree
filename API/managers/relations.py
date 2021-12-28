from database.models import Parent, Sibling
from helpers.decorators import res_err_handler
from helpers.http import Response
from helpers.http.status_codes import Status


@res_err_handler
def create_parent(child_id, parent_id):
    Parent.create(child_id=child_id, parent_id=parent_id)
    return Response.success({'message': 'Parent added successfully.'}, Status.CREATED)


@res_err_handler
def update_parent(child_id, parent_id, new_parent_id):
    parent = Parent.get(child_id=child_id, parent_id=parent_id)
    parent.update(child_id=child_id, parent_id=new_parent_id)
    return Response.success({'message': 'Parent updated successfully.'}, Status.OK)


@res_err_handler
def delete_parent(child_id, parent_id):
    Parent.get(child_id=child_id, parent_id=parent_id).delete()
    return Response.success({'message': 'Parent deleted successfully.'}, Status.OK)


@res_err_handler
def create_sibling(user_id, sibling_id):
    Sibling.create(user_id=user_id, sibling_id=sibling_id)
    return Response.success({'message': 'Sibling added successfully.'}, Status.CREATED)


@res_err_handler
def update_sibling(user_id, sibling_id, new_sibling_id):
    sibling = Sibling.get(user_id=user_id, sibling_id=sibling_id)
    sibling.update(user_id=user_id, sibling_id=new_sibling_id)
    return Response.success({'message': 'Sibling updated successfully.'}, Status.OK)


@res_err_handler
def delete_sibling(user_id, sibling_id):
    Sibling.get(user_id=user_id, sibling_id=sibling_id).delete()
    return Response.success({'message': 'Sibling deleted successfully.'}, Status.OK)
