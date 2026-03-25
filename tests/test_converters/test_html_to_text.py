from ccli.converters.html_to_text import html_to_markdown


def test_empty_input() -> None:
    assert html_to_markdown("") == ""


def test_paragraph() -> None:
    result = html_to_markdown("<p>Hello world</p>")
    assert "Hello world" in result


def test_bold() -> None:
    result = html_to_markdown("<p><strong>Bold</strong> text</p>")
    assert "**Bold**" in result


def test_heading() -> None:
    result = html_to_markdown("<h1>Title</h1>")
    assert "# Title" in result


def test_link() -> None:
    result = html_to_markdown('<a href="https://example.com">link</a>')
    assert "https://example.com" in result
    assert "link" in result


def test_list() -> None:
    result = html_to_markdown("<ul><li>Item 1</li><li>Item 2</li></ul>")
    assert "Item 1" in result
    assert "Item 2" in result


def test_strips_whitespace() -> None:
    result = html_to_markdown("   <p>Hello</p>   ")
    assert result == result.strip()
