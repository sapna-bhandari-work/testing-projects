"""
GET endpoint tests for the JSONPlaceholder API.

Covers:
- GET /posts          — collection endpoint
- GET /posts/1        — single resource, required keys, schema validation
- GET /posts/9999     — 404 handling
- GET /posts?userId=1 — filtered collection
- GET /users/1        — user resource, schema validation
- Response-time SLA assertions on selected requests
"""

import pytest

from utils.schema_validator import validate_schema

# Maximum acceptable response latency in seconds (2 000 ms SLA).
_LATENCY_LIMIT: float = 2.0


# ---------------------------------------------------------------------------
# GET /posts — full collection
# ---------------------------------------------------------------------------


class TestGetAllPosts:
    """Tests for the /posts collection endpoint."""

    def test_status_200(self, api_client):
        """GET /posts must return HTTP 200 OK."""
        response = api_client.get("/posts")
        assert response.status_code == 200

    def test_response_is_list(self, api_client):
        """GET /posts response body must be a JSON array."""
        response = api_client.get("/posts")
        assert isinstance(response.json(), list)

    def test_list_is_not_empty(self, api_client):
        """GET /posts must return at least one item."""
        response = api_client.get("/posts")
        assert len(response.json()) > 0

    def test_response_time_under_sla(self, api_client):
        """GET /posts response time must be under 2 000 ms."""
        response = api_client.get("/posts")
        elapsed = response.elapsed.total_seconds()
        assert elapsed < _LATENCY_LIMIT, (
            f"GET /posts latency {elapsed:.3f}s exceeded SLA of {_LATENCY_LIMIT}s"
        )


# ---------------------------------------------------------------------------
# GET /posts/1 — single post
# ---------------------------------------------------------------------------


class TestGetSinglePost:
    """Tests for the /posts/{id} single-resource endpoint."""

    def test_status_200(self, api_client):
        """GET /posts/1 must return HTTP 200 OK."""
        response = api_client.get("/posts/1")
        assert response.status_code == 200

    def test_required_keys_present(self, api_client):
        """GET /posts/1 response must contain id, title, body, and userId fields."""
        response = api_client.get("/posts/1")
        data = response.json()
        for key in ("id", "title", "body", "userId"):
            assert key in data, f"Required key '{key}' missing from response body"

    def test_schema_matches_post_schema(self, api_client):
        """GET /posts/1 response must conform to post_schema.json (Draft-07)."""
        response = api_client.get("/posts/1")
        validate_schema(response.json(), "post_schema.json")

    def test_response_time_under_sla(self, api_client):
        """GET /posts/1 response time must be under 2 000 ms."""
        response = api_client.get("/posts/1")
        elapsed = response.elapsed.total_seconds()
        assert elapsed < _LATENCY_LIMIT, (
            f"GET /posts/1 latency {elapsed:.3f}s exceeded SLA of {_LATENCY_LIMIT}s"
        )


# ---------------------------------------------------------------------------
# GET /posts/9999 — non-existent resource
# ---------------------------------------------------------------------------


class TestGetNonExistentPost:
    """Tests covering 404 behaviour for unknown post IDs."""

    def test_status_404(self, api_client):
        """GET /posts/9999 must return HTTP 404 Not Found."""
        response = api_client.get("/posts/9999")
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# GET /posts?userId=1 — filtered collection
# ---------------------------------------------------------------------------


class TestGetPostsFilteredByUserId:
    """Tests for query-string filtering on the /posts endpoint."""

    def test_status_200(self, api_client):
        """GET /posts?userId=1 must return HTTP 200 OK."""
        response = api_client.get("/posts", params={"userId": 1})
        assert response.status_code == 200

    def test_all_items_belong_to_user(self, api_client):
        """GET /posts?userId=1 every returned item must have userId == 1."""
        response = api_client.get("/posts", params={"userId": 1})
        items = response.json()
        assert isinstance(items, list) and len(items) > 0, (
            "Filtered response must be a non-empty list"
        )
        for post in items:
            assert post.get("userId") == 1, (
                f"Post id={post.get('id')} has userId={post.get('userId')}, expected 1"
            )


# ---------------------------------------------------------------------------
# GET /users/1 — user resource
# ---------------------------------------------------------------------------


class TestGetUser:
    """Tests for the /users/{id} endpoint."""

    def test_status_200(self, api_client):
        """GET /users/1 must return HTTP 200 OK."""
        response = api_client.get("/users/1")
        assert response.status_code == 200

    def test_schema_matches_user_schema(self, api_client):
        """GET /users/1 response must conform to user_schema.json (Draft-07)."""
        response = api_client.get("/users/1")
        validate_schema(response.json(), "user_schema.json")

    def test_response_time_under_sla(self, api_client):
        """GET /users/1 response time must be under 2 000 ms."""
        response = api_client.get("/users/1")
        elapsed = response.elapsed.total_seconds()
        assert elapsed < _LATENCY_LIMIT, (
            f"GET /users/1 latency {elapsed:.3f}s exceeded SLA of {_LATENCY_LIMIT}s"
        )
