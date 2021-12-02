import logging
import click


LOGGER = logging.getLogger(__name__)


def read_file(filename):
    LOGGER.debug(f"Reading {filename}")

    values = []
    with open(filename) as fin:
        values = [int(x.strip()) for x in fin.readlines()]

    return values


def number_of_increments(values):

    diffs = [b - a for a, b in zip(values[:-1], values[1:])]
    LOGGER.debug(f"Diffs: {diffs}")

    increments = [x > 0 for x in diffs]
    LOGGER.debug(f"Increment?: {increments}")
    return sum(increments)


def apply_window(values, window_size):

    return [
        values[i : min(i + window_size, len(values))] for i in range(0, len(values))
    ]


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def main(filename, debug):

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day 01")
    values = read_file(filename)

    n_increments = number_of_increments(values)
    LOGGER.info(f"Part 01: Amount of increments: {n_increments}")

    values = apply_window(values, 3)
    values = [sum(x) for x in values]

    n_increments = number_of_increments(values)
    LOGGER.info(f"Part 02: Amount of increments: {n_increments}")


if __name__ == "__main__":

    main()
