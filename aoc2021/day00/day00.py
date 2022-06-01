import logging
import click
from collections import namedtuple
import pprint

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def problem(filename, debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day 00")


if __name__ == "__main__":
    problem()
