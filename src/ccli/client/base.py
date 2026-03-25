import time
from typing import Any

import httpx

from ..exceptions import AuthError, ForbiddenError, NetworkError, NotFoundError, RateLimitError

_MAX_RETRIES = 3
_RETRY_BASE_DELAY = 1.0


class ConfluenceClient:
    """Thin wrapper around httpx.Client that maps HTTP errors to domain exceptions
    and retries on rate-limit responses with exponential back-off."""

    def __init__(self, http_client: httpx.Client) -> None:
        self._http = http_client

    def _raise_for_status(self, response: httpx.Response) -> None:
        if response.status_code == 401:
            raise AuthError()
        if response.status_code == 403:
            raise ForbiddenError()
        if response.status_code == 404:
            raise NotFoundError()
        response.raise_for_status()

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        for attempt in range(_MAX_RETRIES + 1):
            try:
                response = self._http.get(path, params=params)
            except httpx.NetworkError as exc:
                raise NetworkError(str(exc)) from exc

            if response.status_code == 429:
                if attempt < _MAX_RETRIES:
                    delay = _RETRY_BASE_DELAY * (2**attempt)
                    try:
                        delay = float(response.headers.get("Retry-After", str(delay)))
                    except ValueError:
                        pass
                    time.sleep(delay)
                    continue
                raise RateLimitError()

            self._raise_for_status(response)
            result: dict[str, Any] = response.json()
            return result

        raise RateLimitError()  # pragma: no cover
