"""
POST endpoint tests for the JSONPlaceholder API.

Covers:
- POST /posts with a valid payload  — HTTP 201, echoed fields, auto-generated id
- POST /posts with an empty body    — HTTP 201 (documented API limitation)
- Response-time SLA assertion

NOTE — JSONPlaceholder API limitation:
    This is a read-only mock API.  POST requests are accepted and a simulated
    response is returned (always with id=101), but no data is actually stored
    server-side.  Tests that verify echoed field values assert the *mock*
    behaviour, not persistence.
"""

import pytest

from data.payloads import EMPTY_POST_PAYLOAD, VALID_POST_PAYLOAD

# Maximum acceptable response latency in seconds (2 000 ms SLA).
_LATENCY_LIMIT: float = 2.0


class TestPostPosts:
    """Tests for the POST /posts endpoint."""

    def test_valid_payload_returns_201(self, api_client):
        """POST /posts with a valid payload must return HTTP 201 Created."""
        response = api_client.post("/posts", payload=VALID_POST_PAYLOAD)
        assert response.status_code == 201

    def test_response_echoes_submitted_title(self, api_client):
        """POST /posts response body must echo the submitted 'title' field."""
        response = api_client.post("/posts", payload=VALID_POST_PAYLOAD)
        data = response.json()
        assert data.get("title") == VALID_POST_PAYLOAD["title"], (
            f"Expected title '{VALID_POST_PAYLOAD['title']}', got '{data.get('title')}'"
        )

    def test_response_echoes_submitted_body(self, api_client):
        """POST /posts response body must echo the submitted 'body' field."""
        response = api_client.post("/posts", payload=VALID_POST_PAYLOAD)
        data = response.json()
        assert data.get("body") == VALID_POST_PAYLOAD["body"], (
            f"Expected body '{VALID_POST_PAYLOAD['body']}', got '{data.get('body')}'"
        )

    def test_response_echoes_submitted_user_id(self, api_client):
        """POST /posts response body must echo the submitted 'userId' field."""
        response = api_client.post("/posts", payload=VALID_POST_PAYLOAD)
        data = response.json()
        assert data.get("userId") == VALID_POST_PAYLOAD["userId"], (
            f"Expected userId={VALID_POST_PAYLOAD['userId']}, got {data.get('userId')}"
        )

    def test_response_contains_auto_generated_id(self, api_client):
        """POST /posts response must include an auto-generated integer 'id' field."""
        response = api_client.post("/posts", payload=VALID_POST_PAYLOAD)
        data = response.json()
        assert "id" in data, "Response body must contain an 'id' field"
        assert isinstance(data["id"], int), (
            f"'id' must be an integer, got {type(data['id']).__name__}"
        )

    def test_empty_body_returns_201(self, api_client):
        """
        POST /posts with an empty body must return HTTP 201.

        DOCUMENTED LIMITATION: JSONPlaceholder is a mock API with no input
        validation.  It accepts any payload — including empty objects — and
        always responds with HTTP 201.  A real production API should return
        HTTP 400 Bad Request when required fields (title, body, userId) are
        absent.  This test pins the *known mock behaviour* so regressions
        against the mock are caught, while the docstring records the expected
        production behaviour for future implementors.
        """
        response = api_client.post("/posts", payload=EMPTY_POST_PAYLOAD)
        assert response.status_code == 201

    def test_response_time_under_sla(self, api_client):
        """POST /posts response time must be under 2 000 ms."""
        response = api_client.post("/posts", payload=VALID_POST_PAYLOAD)
        elapsed = response.elapsed.total_seconds()
        assert elapsed < _LATENCY_LIMIT, (
            f"POST /posts latency {elapsed:.3f}s exceeded SLA of {_LATENCY_LIMIT}s"
        )
