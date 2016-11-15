"""Flask blueprint for / endpoint.

Exposes the blueprint as a module-level variable named `main`.
"""
from flask import Blueprint, redirect

# pylint: disable=invalid-name
main = Blueprint('main', __name__)


@main.route('/')
def home():
    """Redirects home to health check endpoint."""
    return redirect('/health', code=302)
