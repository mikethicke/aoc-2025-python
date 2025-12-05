def solve_part1(input_txt: str) -> int:
    fresh, ingredients = parse_input(input_txt)
    return sum(1 for ingredient in ingredients if is_fresh(ingredient, fresh))


def solve_part2(input_txt: str) -> int:
    fresh, _ = parse_input(input_txt)
    fresh_sorted = sorted(fresh)
    current_start = 0
    current_finish = 0
    total = 0
    for start, finish in fresh_sorted:
        if start > current_finish:
            total += current_finish - current_start + 1
            current_start = start
            current_finish = finish
            continue
        if finish > current_finish:
            current_finish = finish
    total += current_finish - current_start
    return total


def is_fresh(ingredient: int, fresh: list[tuple[int, int]]) -> bool:
    for start, finish in fresh:
        if ingredient >= start and ingredient <= finish:
            return True
    return False


def parse_input(input_txt: str) -> tuple[list[tuple[int, int]], list[int]]:
    fresh_input, available_input = input_txt.split("\n\n")
    fresh = [
        (int(x), int(y))
        for line in fresh_input.splitlines()
        for x, y in [line.split("-")]
    ]
    available = [int(line) for line in available_input.splitlines()]
    return fresh, available
