import logging
import click


LOGGER = logging.getLogger(__name__)


def read_file(filename):
    LOGGER.debug(f"Reading {filename}")
    values = []

    with open(filename) as fin:
        values = [x.strip() for x in fin.readlines()]

    return values


def parse_input(values):
    numbers = [int(x) for x in values[0].split(",")]

    boards = [x for x in values[2:] if len(x)]
    boards = [[int(y) for y in (x.strip().split())] for x in boards]
    boards = [boards[i : i + 5] for i in range(0, len(boards), 5)]

    return numbers, boards


class BingoBoard:
    def __init__(self, matrix):
        self._values = dict()
        for i in range(0,5):
            for j in range(0,5):
                self._values[matrix[i][j]] = (i, j)

        self._rows = [0] * 5
        self._columns = [0] * 5
        self._last_number_marked = None

    def mark_number(self, number):
        if number not in self._values:
            return

        row, column = self._values.pop(number)
        self._rows[row] += 1
        self._columns[column] += 1

        self._last_number_marked = number

    def is_bingo(self):
        if 5 in self._rows + self._columns:
            return True

        return False

    def score(self):
        if self._last_number_marked is None:
            return

        score = sum(self._values.keys()) * self._last_number_marked
        return score


class BingoGame:
    def __init__(self, boards):
        LOGGER.debug(f"Boards: {boards}")
        self._boards = [BingoBoard(board) for board in boards]
        self.winners = list()

    def mark_number(self, number):
        LOGGER.info(f"Checking number {number} in boards.")
        for board in self._boards:
            if board.is_bingo():
                continue

            board.mark_number(number)

            if board.is_bingo():
                LOGGER.info(f"Winner found")
                self.winners.append(board)

@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def main(filename, debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day 04")
    values = read_file(filename)
    numbers, boards = parse_input(values)

    game = BingoGame(boards)
    for number in numbers:
        game.mark_number(number)

    LOGGER.info(f"First Winner score: {game.winners[0].score()}")
    LOGGER.info(f"Last Winner score: {game.winners[-1].score()}")


if __name__ == "__main__":
    main()
