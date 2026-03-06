"""
Request payload definitions for the JSONPlaceholder API test suite.

All request body dictionaries are centralised here so that tests never
embed raw data inline. Import the constants you need directly::

    from data.payloads import VALID_POST_PAYLOAD, UPDATED_POST_PAYLOAD
"""

from typing import Any, Dict

# ---------------------------------------------------------------------------
# POST /posts payloads
# ---------------------------------------------------------------------------

VALID_POST_PAYLOAD: Dict[str, Any] = {
    "title": "Test Post Title",
    "body": "This is the body content of the automated test post.",
    "userId": 1,
}
"""A well-formed post body used for happy-path POST tests."""

EMPTY_POST_PAYLOAD: Dict[str, Any] = {}
"""
Empty payload used to document JSONPlaceholder's permissive validation.

JSONPlaceholder accepts an empty body and returns HTTP 201.  A production
API would normally reject this with HTTP 400 Bad Request.
"""

# ---------------------------------------------------------------------------
# PUT /posts/1 payloads
# ---------------------------------------------------------------------------

UPDATED_POST_PAYLOAD: Dict[str, Any] = {
    "id": 1,
    "title": "Updated Post Title — Automated Test",
    "body": "This is the updated body content sent by the automated PUT test.",
    "userId": 1,
}
"""Full replacement payload for PUT /posts/1 update tests."""
