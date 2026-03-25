import json
from typing import Any


def print_json(data: Any) -> None:
    """Write JSON to stdout. All other output must go to stderr."""
    print(json.dumps(data, ensure_ascii=False, indent=2))
