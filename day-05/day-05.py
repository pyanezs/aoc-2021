import logging
import click
import numpy as np
from collections import namedtuple

Point = namedtuple("Point", "x y")

LOGGER = logging.getLogger(__name__)


def read_file(filename):
    LOGGER.debug(f"Reading {filename}")
    values = []

    with open(filename) as fin:
        values = [x.strip().split(" -> ") for x in fin.readlines()]

    max_x, max_y = 0, 0
    rvalues = list()
    for p1, p2 in values:
        p = [int(x) for x in p1.split(",")]
        p1 = Point(x=p[0], y=p[1])
        p = [int(x) for x in p2.split(",")]
        p2 = Point(x=p[0], y=p[1])
        LOGGER.debug(f"P1: {p1.x} | P2: {p2.x}")

        rvalues.append((p1, p2))
        max_x = max(max_x, p1.x, p2.x)
        max_y = max(max_y, p1.y, p2.y)

    return max_x, max_y, rvalues


class Diagram:
    def __init__(self, x_size, y_size):
        LOGGER.info(f"Dimensions: {x_size} x {y_size}")
        self._diagram = np.array([[0] * (y_size + 1)] * (x_size + 1))

    def add_entry(self, p1, p2, diagonals=False):
        LOGGER.debug(f"Processing: {p1} x {p2}")

        if p1.x == p2.x:
            interval = [min(p1.y, p2.y), max(p1.y, p2.y)]
            for i in range(interval[0], interval[1] + 1):
                self._diagram[i][p1.x] += 1
        elif p1.y == p2.y:
            interval = [min(p1.x, p2.x), max(p1.x, p2.x)]
            for i in range(interval[0], interval[1] + 1):
                LOGGER.debug(f"Adding 1 to cell [{i}][{p1.y}]")
                self._diagram[p1.y][i] += 1
        elif diagonals:
            x_incr = 1 if p2.x > p1.x else -1
            y_incr = 1 if p2.y > p1.y else -1
            for i in range(abs(p2.x - p1.x) + 1):
                LOGGER.debug(f"Adding 1 to cell [{p1.x + x_incr * i}][{p1.y + y_incr * i}]")
                self._diagram[p1.y + y_incr * i][p1.x + x_incr * i] += 1


    def count_greater_than(self, value):
        values = self._diagram.flatten()
        count = [x >= value for x in values]
        return sum(count)

    def __repr__(self):
        value = ""

        for row in self._diagram:
            value += " ".join([str(x) for x in row]) + " \n"
        return value


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def main(filename, debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2022 Day 04")
    x_size, y_size, values = read_file(filename)

    dia = Diagram(x_size, y_size)
    for p1, p2 in values:
        dia.add_entry(p1, p2)

    LOGGER.info(f"Part 1: {dia.count_greater_than(2)}")

    dia = Diagram(x_size, y_size)
    for p1, p2 in values:
        dia.add_entry(p1, p2, diagonals=True)

    LOGGER.info(f"Part 2: {dia.count_greater_than(2)}")


if __name__ == "__main__":
    main()
