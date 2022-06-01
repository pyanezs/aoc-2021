import logging
import click
from collections import namedtuple
import pprint

LOGGER = logging.getLogger(__name__)


def read_file(filename):
    LOGGER.debug(f"Reading {filename}")
    values = []

    with open(filename) as fin:
        values = [x.strip().split(",") for x in fin.readlines()]

    return [int(x) for x in values[0]]


def get_fuel_cost(crabs, position):

    costs = [max(x, position) - min(x, position) for x in crabs]
    return sum(costs)


def get_fuel_cost_p2(crabs, position):

    increments = [max(x, position) - min(x, position) for x in crabs]
    costs = [sum([x for x in range(1, y + 1)]) for y in increments]

    return sum(costs)


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def solve(filename, debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2022 Day 07")
    crabs = read_file(filename)

    min_pos = min(crabs)
    max_pos = max(crabs)

    min_cost = float("Inf")
    min_cost_p2 = float("Inf")
    for i in range(min_pos, max_pos + 1):
        cost = get_fuel_cost(crabs, i)
        min_cost = min(min_cost, cost)
        cost = get_fuel_cost_p2(crabs, i)
        min_cost_p2 = min(min_cost_p2, cost)

    LOGGER.info(f"Min cost to align Part 1: {min_cost}")
    LOGGER.info(f"Min cost to align Part 1: {min_cost_p2}")


if __name__ == "__main__":
    solve()

