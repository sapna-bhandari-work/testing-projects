"""
DELETE endpoint tests for the JSONPlaceholder API.

Covers:
- DELETE /posts/1    — HTTP 200, response body is empty object {}
- DELETE /posts/9999 — HTTP 200 (documented mock limitation)
- Response-time SLA assertion

NOTE — JSONPlaceholder API limitation:
    DELETE requests always return HTTP 200 with an empty JSON object regardless
    of whether the target resource exists.  A production REST API would return:
      - HTTP 200 (or 204) when the resource existed and was deleted.
      - HTTP 404 when the resource was not found.
    Tests in this module pin the *known mock behaviour* and document the
    divergence from production expectations in their docstrings.
"""

import pytest

# Maximum acceptable response latency in seconds (2 000 ms SLA).
_LATENCY_LIMIT: float = 2.0


class TestDeletePost:
    """Tests for the DELETE /posts/{id} endpoint."""

    def test_delete_existing_post_returns_200(self, api_client):
        """DELETE /posts/1 must return HTTP 200 OK."""
        response = api_client.delete("/posts/1")
        assert response.status_code == 200

    def test_delete_existing_post_body_is_empty_object(self, api_client):
        """DELETE /posts/1 response body must be an empty JSON object {}."""
        response = api_client.delete("/posts/1")
        data = response.json()
        assert data == {}, (
            f"Expected empty object {{}}, received: {data}"
        )

    def test_delete_nonexistent_post_returns_200(self, api_client):
        """
        DELETE /posts/9999 must return HTTP 200 OK.

        DOCUMENTED LIMITATION: JSONPlaceholder is a mock API that responds
        with HTTP 200 for *all* DELETE requests, including those targeting
        resources that do not exist (id=9999).  A production REST API should
        return HTTP 404 Not Found in this scenario.  This test asserts and
        documents the known mock behaviour so any deviation is surfaced
        immediately during a regression run.
        """
        response = api_client.delete("/posts/9999")
        assert response.status_code == 200

    def test_response_time_under_sla(self, api_client):
        """DELETE /posts/1 response time must be under 2 000 ms."""
        response = api_client.delete("/posts/1")
        elapsed = response.elapsed.total_seconds()
        assert elapsed < _LATENCY_LIMIT, (
            f"DELETE /posts/1 latency {elapsed:.3f}s exceeded SLA of {_LATENCY_LIMIT}s"
        )
