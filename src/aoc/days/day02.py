def solve_part1(input_text: str) -> int:
    ranges = parse_ranges(input_text)
    sum_invalid = 0
    for start, end in ranges:
        sum_invalid += sum(n for n in range(start, end + 1) if is_invalid(n))
    return sum_invalid


def solve_part2(input_text: str) -> int:
    ranges = parse_ranges(input_text)
    sum_invalid = 0
    for start, end in ranges:
        sum_invalid += sum(n for n in range(start, end + 1) if is_invalid_2(n))
    return sum_invalid


def parse_ranges(input_text: str) -> list[tuple[int, int]]:
    parsed_ranges = []
    for r in input_text.split(","):
        start, end = r.split("-")
        parsed_ranges.append((int(start), int(end)))
    return parsed_ranges


def is_invalid(number: int) -> bool:
    num_str = str(number)
    num_len = len(num_str)
    if num_len % 2 != 0:
        return False
    first_half, second_half = num_str[: num_len // 2], num_str[num_len // 2 :]
    return first_half == second_half


def is_invalid_2(number: int) -> bool:
    num_str = str(number)
    for i in range(1, len(num_str) // 2 + 1):
        if len(num_str) % i != 0:
            continue
        sub_str = num_str[:i]
        if sub_str * (len(num_str) // i) == num_str:
            return True
    return False
