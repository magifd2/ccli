from pytest_httpx import HTTPXMock

from ccli.auth import build_client
from ccli.config import Config, ConfluenceSettings


def _make_config(url: str = "https://example.atlassian.net") -> Config:
    return Config(
        confluence=ConfluenceSettings(url=url, username="user@example.com", api_token="token123")
    )


def test_build_client_base_url() -> None:
    client = build_client(_make_config())
    # Base URL is the domain only; API paths are constructed by callers
    assert str(client.base_url).rstrip("/") == "https://example.atlassian.net"


def test_build_client_auth_header(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response()
    client = build_client(_make_config())
    client.get("/wiki/api/v2/spaces")
    request = httpx_mock.get_requests()[0]
    assert "Authorization" in request.headers
    assert request.headers["Authorization"].startswith("Basic ")


def test_build_client_accept_header() -> None:
    client = build_client(_make_config())
    request = client.build_request("GET", "/wiki/api/v2/spaces")
    assert request.headers["Accept"] == "application/json"


def test_build_client_timeout() -> None:
    client = build_client(_make_config())
    assert client.timeout.read == 30.0
