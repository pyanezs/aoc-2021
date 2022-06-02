import logging
import click
from collections import namedtuple
import pprint
from typing import Tuple

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def solve(filename, debug) -> Tuple[str, str]:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day 00")

    return "Result A", "Result B"


if __name__ == "__main__":
    solve()

