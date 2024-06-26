#!/usr/bin/env python3
""" Module of Authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if len(path) == 0:
            return True

        # Ensure path ends with a slash for comparison consistency
        if not path.endswith('/'):
            path += '/'

        for exc in excluded_paths:
            if len(exc) == 0:
                continue

            # If the excluded path ends with '*', check if path starts with the base of the excluded path
            if exc.endswith('*'):
                if path.startswith(exc[:-1]):
                    return False
            else:
                # Ensure excluded path ends with a slash for comparison consistency
                if not exc.endswith('/'):
                    exc += '/'
                if path == exc:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
