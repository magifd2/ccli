import httpx

from .config import Config

# Path prefixes for Confluence REST APIs
API_V2 = "/wiki/api/v2"
API_V1 = "/wiki/rest/api"


def build_client(config: Config) -> httpx.Client:
    """Build an authenticated httpx client.

    Base URL is the Confluence domain only; callers construct full paths
    using API_V2 or API_V1 prefixes.
    """
    return httpx.Client(
        base_url=config.confluence.url,
        auth=(config.confluence.username, config.confluence.api_token),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        timeout=30.0,
    )
