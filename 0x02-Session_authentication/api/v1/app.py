#!/usr/bin/env python3
"""
Route module for the API.
Handles routing, authentication selection, and error responses.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

# Create the Flask application
app = Flask(__name__)

# Register blueprint for API routes
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for specific routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Select authentication method based on environment variable
auth = getenv("AUTH_TYPE", None)

# Conditional import and instantiation of the appropriate authentication class
if auth == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_auth():
    """
    A method to handle authentication before processing a request.
    Checks if the incoming request path requires authentication.
    If so, verifies that an authorization header is present and that
    the user is authenticated; otherwise, returns an error response.

    Returns:
        HTTP 401 if authorization header is missing or unauthorized,
        HTTP 403 if user authentication fails
    """
    # List of paths that do not require authentication
    authl = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    # Skip further checks if no authentication method is configured
    if auth is None:
        return

    # Bypass authentication for exempt paths
    if not auth.require_auth(request.path, authl):
        return

    # Check for the presence of an authorization header
    if auth.authorization_header(request) is None:
        abort(401)

    # Ensure the current user is authenticated
    if auth.current_user(request) is None:
        abort(403)
    
    request.current_user = auth.current_user(request)


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found error handler. Returns JSON error response with
    HTTP 404 status.
    """
    return jsonify({"error": "Not found"}), 404


# Error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized_access(error) -> str:
    """ Unauthorized error handler. Returns JSON error response
    with HTTP 401 status.
    """
    return jsonify({"error": "Unauthorized"}), 401


# Error handler for 403 Forbidden
@app.errorhandler(403)
def forbidden_access(error) -> str:
    """ Forbidden access error handler. Returns JSON error response with
    HTTP 403 status.
    """
    return jsonify({"error": "Forbidden"}), 403


# Run the application if this module is executed directly
if __name__ == "__main__":
    # Retrieve host and port from environment variables with default values
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")

    # Start Flask application with specified host and port
    app.run(host=host, port=port)
