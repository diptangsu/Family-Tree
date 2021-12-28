from functools import wraps
from typing import Callable

from helpers.http import Response


def res_err_handler(func: Callable) -> Callable:
    """Response error handler function.

    Args:
        func (Callable): A function that returns the main response for an endpoint.

    Returns:
        Callable: Function extended with an error handler.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            msg, *args = err.args
            err_args = (str(msg),)
            if args:
                err_args = (*err_args, *args)
            return Response.error(*err_args)

    return wrapper
