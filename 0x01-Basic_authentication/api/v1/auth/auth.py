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
            check for Authorization
        """
        if path is None or excluded_paths is None:
            return True
        np = f"{path}/"
        nep = [excluded_paths.rstrip('/') for excluded_p in excluded_paths]
        if np not in nep:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
            Handle request header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Retrieve the User sending request
        """
        return None
