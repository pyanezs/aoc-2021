import logging
import click
from collections import namedtuple
import pprint

LOGGER = logging.getLogger(__name__)


def get_fuel_cost_p2(crabs, position):

    increments = [max(x, position) - min(x, position) for x in crabs]
    costs = [sum([x for x in range(1, y + 1)]) for y in increments]

    return sum(costs)


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def main(filename, debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day Test")


if __name__ == "__main__":
    main()
