"""
PUT endpoint tests for the JSONPlaceholder API.

Covers:
- PUT /posts/1 with an updated payload — HTTP 200, title echoed, id matches route
- Response-time SLA assertion

NOTE — JSONPlaceholder API limitation:
    PUT requests are accepted and the expected resource is returned in the
    response, but no data is persisted server-side.  A subsequent GET /posts/1
    will still return the original data.
"""

import pytest

from data.payloads import UPDATED_POST_PAYLOAD

# Maximum acceptable response latency in seconds (2 000 ms SLA).
_LATENCY_LIMIT: float = 2.0


class TestPutPost:
    """Tests for the PUT /posts/{id} endpoint."""

    def test_returns_200(self, api_client):
        """PUT /posts/1 must return HTTP 200 OK."""
        response = api_client.put("/posts/1", payload=UPDATED_POST_PAYLOAD)
        assert response.status_code == 200

    def test_response_title_matches_sent_value(self, api_client):
        """PUT /posts/1 response 'title' must equal the value sent in the request body."""
        response = api_client.put("/posts/1", payload=UPDATED_POST_PAYLOAD)
        data = response.json()
        assert data.get("title") == UPDATED_POST_PAYLOAD["title"], (
            f"Expected title '{UPDATED_POST_PAYLOAD['title']}', got '{data.get('title')}'"
        )

    def test_response_id_matches_route(self, api_client):
        """PUT /posts/1 response 'id' must equal 1 (the route parameter)."""
        response = api_client.put("/posts/1", payload=UPDATED_POST_PAYLOAD)
        data = response.json()
        assert data.get("id") == 1, (
            f"Expected id=1, got id={data.get('id')}"
        )

    def test_response_time_under_sla(self, api_client):
        """PUT /posts/1 response time must be under 2 000 ms."""
        response = api_client.put("/posts/1", payload=UPDATED_POST_PAYLOAD)
        elapsed = response.elapsed.total_seconds()
        assert elapsed < _LATENCY_LIMIT, (
            f"PUT /posts/1 latency {elapsed:.3f}s exceeded SLA of {_LATENCY_LIMIT}s"
        )
