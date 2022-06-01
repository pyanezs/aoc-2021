import logging
import click


LOGGER = logging.getLogger(__name__)


def read_file(filename):
    LOGGER.debug(f"Reading {filename}")
    values = []

    with open(filename) as fin:
        values = [[int(y) for y in x.strip()] for x in fin.readlines()]

    return values


def sum_bits(values):
    result = [0] * len(values[0])
    for bits in values:
        for index, value in enumerate(bits):
            result[index] += value

    return result


def to_decimal(bits):
    r_bits = reversed(bits)
    result = [bit * (2 ** i) for i, bit in enumerate(r_bits)]
    return sum(result)


def get_gamma(bits_freq, n_values):
    gamma = [1 if x > n_values / 2 else 0 for x in bits_freq]
    LOGGER.debug(f"Gamma bits: {gamma}")
    return to_decimal(gamma)


def get_epsilon(bits_freq, n_values):
    epsilon = [0 if x > n_values / 2 else 1 for x in bits_freq]
    LOGGER.debug(f"Epsilon bits: {epsilon}")
    return to_decimal(epsilon)


def oxygen_generator_rating(values):
    rval = [x for x in values]
    n_bits = len(values[0])

    for i in range(n_bits):
        freq = sum_bits(rval)
        most_frequent = 1 if freq[i] >= len(rval) / 2 else 0
        LOGGER.debug(f"Remaining elements: {len(rval)} | Freq: {freq}")
        rval = [x for x in rval if x[i] == most_frequent]

    LOGGER.debug(f"Oxygen: {rval}")
    return to_decimal(rval[0])


def co2_scrubber_rating(values):
    rval = [x for x in values]
    n_bits = len(values[0])

    for i in range(n_bits):
        freq = sum_bits(rval)
        most_frequent = 0 if freq[i] >= len(rval) / 2 else 1
        LOGGER.debug(f"Remaining elements: {len(rval)} | Freq: {freq}")
        rval = [x for x in rval if x[i] == most_frequent]
        if len(rval) == 1:
            break

    LOGGER.debug(f"Oxygen: {rval}")
    return to_decimal(rval[0])


@click.command()
@click.option("--filename", help="Input file.")
@click.option("--debug/--no-debug", default=False)
def main(filename, debug):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    LOGGER.info("AOC 2021 Day 03")
    values = read_file(filename)

    bits_freq = sum_bits(values)
    LOGGER.debug(f"Freq: {bits_freq}")

    gamma = get_gamma(bits_freq, len(values))
    epsilon = get_epsilon(bits_freq, len(values))
    LOGGER.info(f"Gamma: {gamma} | Epsilon: {epsilon} | Answer: {gamma * epsilon}")

    oxygen = oxygen_generator_rating(values)
    co2 = co2_scrubber_rating(values)
    LOGGER.info(f"Oxygen: {oxygen} | CO2: {co2} | Ansert: {oxygen * co2}")


if __name__ == "__main__":
    main()
