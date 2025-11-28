import argparse
import importlib
from pathlib import Path

INPUTS_DIR = Path(__file__).resolve().parents[2] / "inputs"  # project_root/inputs


def run_day(day: int, part: int | None = None, sample: bool = False):
    mod_name = f"aoc.days.day{day:02d}"
    try:
        mod = importlib.import_module(mod_name)
    except ModuleNotFoundError as e:
        raise SystemExit(
            f"Day {day:02d} not found. Create src/aoc/days/day{day:02d}.py"
        ) from e

    # By convention, each day module exposes solve(input_text) or solve_part1/solve_part2.
    filename = f"day{day:02d}_sample.txt" if sample else f"day{day:02d}.txt"
    input_path = INPUTS_DIR / filename
    if not input_path.exists():
        raise SystemExit(
            f"Missing input file: {input_path}. Put your {'sample ' if sample else ''}puzzle input there."
        )

    input_text = input_path.read_text().rstrip("\n")

    if part in (None, 1, 2) and hasattr(mod, "solve"):
        # One-function style that returns (part1, part2)
        p1, p2 = mod.solve(input_text)
        if part in (None, 1):
            print(p1)
        if part in (None, 2):
            print(p2)
    else:
        # Two-function style solve_part1 / solve_part2
        if part in (None, 1):
            if not hasattr(mod, "solve_part1"):
                raise SystemExit(f"{mod_name} has no solve_part1")
            print(mod.solve_part1(input_text))
        if part in (None, 2):
            if not hasattr(mod, "solve_part2"):
                raise SystemExit(f"{mod_name} has no solve_part2")
            print(mod.solve_part2(input_text))


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("day", type=int, help="Day number (1..25)")
    parser.add_argument(
        "--part", "-p", type=int, choices=(1, 2), help="Run only part 1 or 2"
    )
    parser.add_argument(
        "--sample",
        "-s",
        action="store_true",
        help="Use sample input (dayXX_sample.txt)",
    )
    args = parser.parse_args()
    run_day(args.day, args.part, args.sample)
