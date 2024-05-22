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

        l_path = len(path)
        if l_path == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
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
