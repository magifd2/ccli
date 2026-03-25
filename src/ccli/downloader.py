from pathlib import Path

import httpx


def download_file(http_client: httpx.Client, url: str, dest: Path) -> None:
    """Stream-download *url* to *dest*, creating parent directories as needed."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with http_client.stream("GET", url) as response:
        response.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in response.iter_bytes(chunk_size=8192):
                if chunk:
                    f.write(chunk)
