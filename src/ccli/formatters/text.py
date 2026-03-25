from rich.console import Console
from rich.table import Table

from ..client.spaces import Space


def print_spaces(spaces: list[Space], *, color: bool = True) -> None:
    console = Console(highlight=False, no_color=not color)
    if not spaces:
        console.print("No spaces found.")
        return

    table = Table(show_header=True, header_style="bold" if color else "", box=None, pad_edge=False)
    table.add_column("KEY", min_width=8)
    table.add_column("NAME", min_width=24)
    table.add_column("TYPE", min_width=8)
    table.add_column("STATUS")

    for space in spaces:
        table.add_row(space.key, space.name, space.type, space.status)

    console.print(table)
