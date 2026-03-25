from markdownify import markdownify


def html_to_markdown(html: str) -> str:
    """Convert HTML string to Markdown. Returns empty string for empty input."""
    if not html:
        return ""
    return markdownify(html, heading_style="ATX", bullets="-").strip()
