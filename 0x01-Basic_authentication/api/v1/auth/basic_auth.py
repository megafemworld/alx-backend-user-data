#!/usr/bin/env python3
"""
    class BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
        BasicAuth inherit from Auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
             returns the Base64 part of the Authorization header
             for a Basic Authentication:
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            delt = "Basic "
            return authorization_header.split(delt, 1)[-1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
            decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decode_b = base64.b64decode(base64_authorization_header)
            return decode_b.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
            returns the user email and password
            from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return tuple(decoded_base64_authorization_header.split(':')
