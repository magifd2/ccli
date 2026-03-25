import os
import sys


def is_tty() -> bool:
    return sys.stdout.isatty()


def use_color() -> bool:
    """Return True when color output is appropriate (tty and NO_COLOR not set)."""
    if os.environ.get("NO_COLOR"):
        return False
    return is_tty()
