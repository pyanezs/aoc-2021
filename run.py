import importlib
import click
from pathlib import Path

for day in range(1, 8):
    day_str = f"day{str(day).zfill(2)}"
    try:
        problem_module = importlib.import_module(f"aoc2021.{day_str}")
    except ModuleNotFoundError:
        print(f"No solution for day {day}")
        continue

    input_file = Path(f"inputs/{day_str}/input.txt")

    print(f"Solving day {day} | Input: {input_file}")
    problem_module.solve(input_file)



