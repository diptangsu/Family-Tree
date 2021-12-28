"""Base Response to manage a single standard of Response throughout the API."""
import json
from typing import Any, Dict, Optional

from flask.wrappers import Response as _Response

from .status_codes import Status, get_status_message


class Response:
    """Replace flask.wrappers.Response.

    Contains dedicated methods for success and error responses.
    Used to maintain uniform response structure in the entire API.
    """

    @staticmethod
    def success(
        result: Any,
        status: Optional[int] = Status.OK,
        headers: Optional[Dict[str, str]] = None,
    ) -> _Response:
        """Global success response.

        Args:
            result (Any): Result to be returned to user.
            status (Optional[int]): HTTP Response Code. Defaults to Status.OK.
            headers (Optional[Dict[str, str]]): Additional Headers. Defaults to None.

        Returns:
            _Response: Custom structured API response.
        """
        if headers is None:
            headers = {}

        http_response = _Response(
            response=json.dumps(
                {'result': result, 'status': get_status_message(status)}
            ),
            status=status,
            headers={'Content-Type': 'text/json', **headers},
        )
        return http_response

    @staticmethod
    def error(
        err: str,
        status: Optional[int] = Status.BAD_REQUEST,
        headers: Optional[Dict[str, str]] = None,
    ) -> _Response:
        """Global error response.

        Args:
            err (Any): Error message to be returned to user.
            status (Optional[int]): HTTP Response Code. Defaults to Status.OK.
            headers (Optional[Dict[str, str]]): Additional Headers. Defaults to None.

        Returns:
            _Response: Custom structured API error response.
        """
        if headers is None:
            headers = {}

        err_response = _Response(
            response=json.dumps(
                {'error': {'message': err}, 'status': get_status_message(status)}
            ),
            status=status,
            headers={'Content-Type': 'text/json', **headers},
        )
        return err_response
