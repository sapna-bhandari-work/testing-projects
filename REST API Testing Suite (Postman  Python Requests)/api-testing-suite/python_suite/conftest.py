"""
PyTest configuration and shared fixtures for the JSONPlaceholder test suite.

Session-scoped fixtures defined here are automatically available to every
test without explicit imports.
"""

import pytest

from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    """
    Session-scoped fixture that provides a single :class:`ApiClient` instance.

    Using session scope means the same ``requests.Session`` (and its
    underlying TCP connection pool) is reused across all tests, which
    reduces connection overhead and keeps the suite fast.

    The base URL defaults to ``https://jsonplaceholder.typicode.com`` but can
    be overridden by setting the ``API_BASE_URL`` environment variable before
    running pytest.

    Returns:
        ApiClient: A fully configured client ready to make HTTP requests.
    """
    return ApiClient()
