def solve_part1(input_text: str) -> int:
    return sum(joltage(line) for line in input_text.splitlines())


def solve_part2(input_text: str) -> int:
    return sum(joltage_12(line) for line in input_text.splitlines())


def joltage(line: str) -> int:
    tens_candidates = line[:-1]
    tens_digit = str(max(int(t) for t in tens_candidates))
    tens_digit_position = tens_candidates.index(tens_digit)
    ones_digit_candidates = line[tens_digit_position + 1 :]
    ones_digit = str(max(int(o) for o in ones_digit_candidates))
    # print(f"line:{line} {tens_digit}{ones_digit}")
    return int(tens_digit + ones_digit)


def joltage_12(line: str) -> int:
    working_line = line
    the_joltage = ""
    last_position = -1
    for digit_num in range(0, 12):
        working_line = working_line[last_position + 1 :]
        # print(
        #     f"digit_num: {digit_num} working_line: {working_line} len wl: {len(working_line)}"
        # )
        slice_off = 11 - digit_num
        if slice_off > 0:
            slice = working_line[:-slice_off]
        else:
            slice = working_line
        biggest_digit = str(max(int(t) for t in slice))
        # print(f"biggest_digit: {biggest_digit}")
        the_joltage += biggest_digit
        last_position = working_line.index(biggest_digit)
    # print(f"line: {line} joltage: {the_joltage}")
    return int(the_joltage)
