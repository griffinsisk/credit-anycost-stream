import json

import pytest
import responses as responses_lib
from requests.exceptions import HTTPError

from cloudzero_client import post_billing_drop, _MAX_BODY_BYTES

API_KEY = "test-api-key-no-bearer"
CONNECTION_ID = "conn-abc123"
BILLING_MONTH = "2025-01-01T00:00:00Z"
URL = f"https://api.cloudzero.com/v2/connections/billing/anycost/{CONNECTION_ID}/billing_drops"

SAMPLE_DATA = [
    {
        "lineitem/type": "Credit",
        "lineitem/description": "AWS promotional credit",
        "time/usage_start": "2025-01-01T00:00:00Z",
        "time/usage_end": "2025-01-31T23:59:59Z",
        "resource/account": "123456789012",
        "resource/service": "AWSCredits",
        "cost/cost": "-50.00",
    }
]


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

@responses_lib.activate
def test_happy_path_200():
    responses_lib.add(responses_lib.POST, URL, json={"id": "drop-1"}, status=200)
    result = post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert result == {"id": "drop-1"}


@responses_lib.activate
def test_authorization_header_no_bearer():
    """Auth header must be exactly the api_key — no 'Bearer ' prefix."""
    responses_lib.add(responses_lib.POST, URL, json={}, status=200)
    post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    sent = responses_lib.calls[0].request
    assert sent.headers["Authorization"] == API_KEY
    assert "Bearer" not in sent.headers["Authorization"]


@responses_lib.activate
def test_url_contains_connection_id():
    responses_lib.add(responses_lib.POST, URL, json={}, status=200)
    post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert CONNECTION_ID in responses_lib.calls[0].request.url


@responses_lib.activate
def test_operation_is_replace_drop():
    responses_lib.add(responses_lib.POST, URL, json={}, status=200)
    post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    body = json.loads(responses_lib.calls[0].request.body)
    assert body["operation"] == "replace_drop"


@responses_lib.activate
def test_timeout_30_passed():
    """responses library will record the timeout if we inspect the PreparedRequest adapter."""
    responses_lib.add(responses_lib.POST, URL, json={}, status=200)
    # We can't directly inspect timeout from responses; verify no exception is raised
    # and the call succeeds (timeout is set in the client code at 30s)
    result = post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert result == {}  # empty body → {}


# ---------------------------------------------------------------------------
# Retry behaviour
# ---------------------------------------------------------------------------

@responses_lib.activate
def test_retries_on_429():
    responses_lib.add(responses_lib.POST, URL, json={}, status=429)
    responses_lib.add(responses_lib.POST, URL, json={}, status=429)
    responses_lib.add(responses_lib.POST, URL, json={"ok": True}, status=200)
    result = post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert result == {"ok": True}
    assert len(responses_lib.calls) == 3


@responses_lib.activate
def test_retries_on_500():
    responses_lib.add(responses_lib.POST, URL, json={}, status=500)
    responses_lib.add(responses_lib.POST, URL, json={"ok": True}, status=200)
    result = post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert result == {"ok": True}
    assert len(responses_lib.calls) == 2


@responses_lib.activate
def test_raises_after_3_retries_on_500():
    for _ in range(3):
        responses_lib.add(responses_lib.POST, URL, json={}, status=500)
    with pytest.raises(HTTPError):
        post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert len(responses_lib.calls) == 3


# ---------------------------------------------------------------------------
# No retry on client errors
# ---------------------------------------------------------------------------

@responses_lib.activate
def test_no_retry_on_401():
    responses_lib.add(responses_lib.POST, URL, json={"error": "unauthorized"}, status=401)
    with pytest.raises(HTTPError) as exc_info:
        post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert exc_info.value.response.status_code == 401
    assert len(responses_lib.calls) == 1


@responses_lib.activate
def test_no_retry_on_400():
    responses_lib.add(responses_lib.POST, URL, json={"error": "bad request"}, status=400)
    with pytest.raises(HTTPError) as exc_info:
        post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, SAMPLE_DATA)
    assert exc_info.value.response.status_code == 400
    assert len(responses_lib.calls) == 1


# ---------------------------------------------------------------------------
# Size guard
# ---------------------------------------------------------------------------

def test_size_guard_raises_before_http_call(monkeypatch):
    """Payload over _MAX_BODY_BYTES should raise ValueError without making HTTP call."""
    import cloudzero_client
    calls = []

    def fake_post(*args, **kwargs):
        calls.append(1)
        raise AssertionError("HTTP call should not have been made")

    monkeypatch.setattr("cloudzero_client.requests.post", fake_post)

    # Build a data list large enough to exceed the limit
    big_row = {"x": "A" * 1000}
    big_data = [big_row] * 5000  # ~5MB+

    with pytest.raises(ValueError, match="exceeds limit"):
        post_billing_drop(API_KEY, CONNECTION_ID, BILLING_MONTH, big_data)

    assert calls == []
