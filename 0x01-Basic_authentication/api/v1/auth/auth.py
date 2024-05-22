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

        slash_path = True if path[- 1] == '/' else False

        if not slash_path:
            path += '/'

        for exc in excluded_paths:
            if len(exc) == 0:
                continue

            if exc[- 1] != '*':
                if path == exc:
                    return False
            if exc[-1] != '/':
                exc += '/'

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
