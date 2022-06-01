import logging
import click
from collections import namedtuple
import pprint

LOGGER = logging.getLogger(__name__)


class School:
    def __init__(self, fish_counters):
        self._days_till_spawn = {i: 0 for i in range(-1, 9)}

        for i in fish_counters:
            self._days_till_spawn[i] += 1

        self.days = 0
        LOGGER.debug(f"Initial state: {sum(self._days_till_spawn.values())}")

    def increment_day(self):
        self.days += 1

        new = {i: 0 for i in range(-1, 9)}
        for i in range(0, 9):
            new[i - 1] += self._days_till_spawn[i]

        new[8] += new[-1]
        new[6] += new[-1]
        new[-1] = 0

        self._days_till_spawn = {k: v for k,v in new.items()}
        LOGGER.info(f"After {self.days} days Total Fish: {sum(new.values())}")


@click.command()
@click.option("--debug/--no-debug", default=False)
def solve(debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2022 Day 06")

    fishes = [
        1,
        1,
        3,
        5,
        3,
        1,
        1,
        4,
        1,
        1,
        5,
        2,
        4,
        3,
        1,
        1,
        3,
        1,
        1,
        5,
        5,
        1,
        3,
        2,
        5,
        4,
        1,
        1,
        5,
        1,
        4,
        2,
        1,
        4,
        2,
        1,
        4,
        4,
        1,
        5,
        1,
        4,
        4,
        1,
        1,
        5,
        1,
        5,
        1,
        5,
        1,
        1,
        1,
        5,
        1,
        2,
        5,
        1,
        1,
        3,
        2,
        2,
        2,
        1,
        4,
        1,
        1,
        2,
        4,
        1,
        3,
        1,
        2,
        1,
        3,
        5,
        2,
        3,
        5,
        1,
        1,
        4,
        3,
        3,
        5,
        1,
        5,
        3,
        1,
        2,
        3,
        4,
        1,
        1,
        5,
        4,
        1,
        3,
        4,
        4,
        1,
        2,
        4,
        4,
        1,
        1,
        3,
        5,
        3,
        1,
        2,
        2,
        5,
        1,
        4,
        1,
        3,
        3,
        3,
        3,
        1,
        1,
        2,
        1,
        5,
        3,
        4,
        5,
        1,
        5,
        2,
        5,
        3,
        2,
        1,
        4,
        2,
        1,
        1,
        1,
        4,
        1,
        2,
        1,
        2,
        2,
        4,
        5,
        5,
        5,
        4,
        1,
        4,
        1,
        4,
        2,
        3,
        2,
        3,
        1,
        1,
        2,
        3,
        1,
        1,
        1,
        5,
        2,
        2,
        5,
        3,
        1,
        4,
        1,
        2,
        1,
        1,
        5,
        3,
        1,
        4,
        5,
        1,
        4,
        2,
        1,
        1,
        5,
        1,
        5,
        4,
        1,
        5,
        5,
        2,
        3,
        1,
        3,
        5,
        1,
        1,
        1,
        1,
        3,
        1,
        1,
        4,
        1,
        5,
        2,
        1,
        1,
        3,
        5,
        1,
        1,
        4,
        2,
        1,
        2,
        5,
        2,
        5,
        1,
        1,
        1,
        2,
        3,
        5,
        5,
        1,
        4,
        3,
        2,
        2,
        3,
        2,
        1,
        1,
        4,
        1,
        3,
        5,
        2,
        3,
        1,
        1,
        5,
        1,
        3,
        5,
        1,
        1,
        5,
        5,
        3,
        1,
        3,
        3,
        1,
        2,
        3,
        1,
        5,
        1,
        3,
        2,
        1,
        3,
        1,
        1,
        2,
        3,
        5,
        3,
        5,
        5,
        4,
        3,
        1,
        5,
        1,
        1,
        2,
        3,
        2,
        2,
        1,
        1,
        2,
        1,
        4,
        1,
        2,
        3,
        3,
        3,
        1,
        3,
        5,
    ]

    school = School(fishes)
    for _ in range(0, 256):
        school.increment_day()


if __name__ == "__main__":
    solve()
