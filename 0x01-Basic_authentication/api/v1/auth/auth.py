#!/usr/bin/env python3
"""
     class to manage the API authentication
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """"
        class is the for authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Check for Authorization
        """
        if path is None or not excluded_paths or excluded_paths == []:
            return True
        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path.rstrip('*')):
                    return False
            elif path == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            Handle request header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Retrieve the User sending request
        """
        return None
