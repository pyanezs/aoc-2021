import logging
import click
from collections import namedtuple


LOGGER = logging.getLogger(__name__)

Command = namedtuple("Command", "action value")


def read_file(filename):
    LOGGER.debug(f"Reading {filename}")
    values = []

    with open(filename) as fin:
        values = [Command(*x.strip().split(" ")) for x in fin.readlines()]

    return values


class Submarine:
    def __init__(self, horizontal_pos=0, depth=0, aim=None):
        self._horizontal_pos = horizontal_pos
        self._depth = depth
        self._aim = aim

    def down(self, value):
        if self._aim is None:
            self._depth += value
        else:
            self._aim += value

    def up(self, value):
        if self._aim is None:
            self._depth -= value
        else:
            self._aim -= value

    def forward(self, value):
        self._horizontal_pos += value

        if self._aim is not None:
            self._depth += self._aim * value

    def process_command(self, command):
        action = command.action
        value = int(command.value)

        if action == "forward":
            self.forward(value)
        elif action == "down":
            self.down(value)
        elif action == "up":
            self.up(value)
        else:
            LOGGER.error(f"Command not valid: {action} {value}")

        LOGGER.debug(
            f"Position: {self._horizontal_pos} | Depth: {self._depth} | Aim: {self._aim}"
        )

    @property
    def horizontal_pos(self):
        return self._horizontal_pos

    @property
    def depth(self):
        return self._depth

    @property
    def aim(self):
        return self._aim


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def main(filename, debug):

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day 02")
    commands = read_file(filename)

    submarine = Submarine()
    for command in commands:
        submarine.process_command(command)
    LOGGER.info(
        f"Final position: {submarine.horizontal_pos} | Depth: {submarine.depth}"
    )
    LOGGER.info(f"Part 1 Answer: {submarine.horizontal_pos * submarine.depth}")

    submarine = Submarine(aim=0)
    for command in commands:
        submarine.process_command(command)
    LOGGER.info(
        f"Final position: {submarine.horizontal_pos} | Depth: {submarine.depth}"
    )
    LOGGER.info(f"Part 2 Answer: {submarine.horizontal_pos * submarine.depth}")


if __name__ == "__main__":
    main()
