from math import prod


def solve_part1(input_txt: str) -> int:
    total = 0
    problems = parse_problems(input_txt)
    for op, term_list in problems:
        if op == "+":
            total += sum(term_list)
        else:
            total += prod(term_list)
    return total


def solve_part2(input_txt: str) -> int:
    total = 0
    problems = cephalapod_parse(input_txt)
    for op, term_list in problems:
        if op == "+":
            total += sum(term_list)
        else:
            total += prod(term_list)
    return total


def parse_problems(input_txt: str) -> list[tuple[str, list[int]]]:
    lines = input_txt.splitlines()
    operations = lines[len(lines) - 1].split()
    term_lists = []
    for line in lines:
        for j, term in enumerate(line.split()):
            if term in ["+", "*"]:
                break
            if len(term_lists) < j + 1:
                term_lists.append([])
            term_lists[j].append(int(term))
    return list(zip(operations, term_lists))


def cephalapod_parse(input_txt: str) -> list[tuple[str, list[int]]]:
    """
    Note: This requires all lines to be equal width, which might not be the case
    depending on how the input was saved. You might need to manually pad the last
    line.
    """
    lines = input_txt.splitlines()
    width = len(lines[0])
    columns = []
    for col in range(width - 1, -1, -1):
        col_txt = "".join([line[col] for line in lines])
        columns.append(col_txt.strip())
    problems = []
    operation = ""
    terms = []
    for column in columns:
        if column == "":
            problems.append((operation, terms))
            operation = ""
            terms = []
            continue
        if column[len(column) - 1] in ["*", "+"]:
            operation = column[len(column) - 1]
            column = column[:-1]
        terms.append(int(column))
    problems.append((operation, terms))
    return problems
