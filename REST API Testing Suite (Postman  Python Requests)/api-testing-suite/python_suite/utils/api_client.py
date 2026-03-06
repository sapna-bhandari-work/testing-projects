"""
API Client module wrapping the Requests library.

Provides a reusable ApiClient class with configurable base URL and
convenience methods for GET, POST, PUT, and DELETE HTTP operations.
"""

import os
from typing import Any, Dict, Optional

import requests

BASE_URL: str = os.environ.get(
    "API_BASE_URL", "https://jsonplaceholder.typicode.com"
)


class ApiClient:
    """
    A reusable HTTP API client that wraps the requests library.

    The base URL defaults to the JSONPlaceholder public API but can be
    overridden via the ``API_BASE_URL`` environment variable or by passing
    a value explicitly to the constructor.

    Example::

        client = ApiClient()
        response = client.get("/posts/1")
        print(response.json())
    """

    def __init__(self, base_url: str = BASE_URL) -> None:
        """
        Initialise the ApiClient with a base URL.

        Args:
            base_url: The root URL for all API requests. Trailing slashes
                are stripped automatically.
        """
        self.base_url: str = base_url.rstrip("/")
        self.session: requests.Session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json",
            }
        )

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _url(self, endpoint: str) -> str:
        """
        Build a fully-qualified URL from the base URL and an endpoint path.

        Args:
            endpoint: The path component (e.g. ``"/posts/1"``).

        Returns:
            The complete URL string.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    # ------------------------------------------------------------------
    # Public HTTP methods
    # ------------------------------------------------------------------

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """
        Perform an HTTP GET request.

        Args:
            endpoint: The API endpoint path (e.g. ``"/posts"``).
            params: Optional mapping of query-string parameters.

        Returns:
            The :class:`requests.Response` object.
        """
        return self.session.get(self._url(endpoint), params=params)

    def post(
        self,
        endpoint: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """
        Perform an HTTP POST request.

        Args:
            endpoint: The API endpoint path (e.g. ``"/posts"``).
            payload: The JSON-serialisable request body as a Python dict.
                Pass ``None`` or ``{}`` to send an empty body.

        Returns:
            The :class:`requests.Response` object.
        """
        return self.session.post(self._url(endpoint), json=payload)

    def put(
        self,
        endpoint: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """
        Perform an HTTP PUT request.

        Args:
            endpoint: The API endpoint path (e.g. ``"/posts/1"``).
            payload: The JSON-serialisable request body as a Python dict.

        Returns:
            The :class:`requests.Response` object.
        """
        return self.session.put(self._url(endpoint), json=payload)

    def delete(self, endpoint: str) -> requests.Response:
        """
        Perform an HTTP DELETE request.

        Args:
            endpoint: The API endpoint path (e.g. ``"/posts/1"``).

        Returns:
            The :class:`requests.Response` object.
        """
        return self.session.delete(self._url(endpoint))
