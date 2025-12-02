import math
import re


def solve_part1(input_text: str) -> int:
    directions = [parse_line(line) for line in input_text.splitlines()]
    position = 50
    zeros = 0
    for delta in directions:
        position = (position + delta) % 100
        if position == 0:
            zeros += 1
    return zeros


def solve_part2(input_text: str) -> int:
    directions = [parse_line(line) for line in input_text.splitlines()]
    position = 50
    zeros = 0
    for delta in directions:
        if position == 0 and delta < 1:
            zeros -= 1
        extra_rotations = math.floor(abs(delta) / 100)
        zeros += extra_rotations
        delta = delta % ((1 if delta >= 0 else -1) * 100)
        if position + delta > 100 or position + delta < 0:
            zeros += 1
        position = (position + delta) % 100
        if position == 0:
            zeros += 1
    return zeros


def parse_line(line: str) -> int:
    match = re.search(r"(.)(\d+)", line)
    if not match:
        raise ValueError(f"Failed to parse line: {line}")
    sign, dir = match.groups()
    if sign == "L":
        return int(dir) * -1
    else:
        return int(dir)
