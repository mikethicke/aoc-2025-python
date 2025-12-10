def solve_part1(input_txt: str) -> int:
    tiles = parse_input(input_txt)
    areas = [
        calc_area(first, second)
        for i, first in enumerate(tiles)
        for second in tiles[i + 1 :]
    ]
    return max(areas)


def solve_part2(input_txt: str) -> int:
    print("Solving part 2...")
    tiles = parse_input(input_txt)
    print("Making perimiter...")
    perimiter = make_perimiter(tiles)
    print("Calculating areas...")
    max_area = 0
    for i, first in enumerate(tiles):
        print(f"tile: {i}")
        for second in tiles[i + 1 :]:
            max_area = calc_new_max(first, second, perimiter, max_area)
    return max_area


def rect_in_poly(
    first_point: tuple, second_point: tuple, perimiter: set[tuple]
) -> bool:
    max_x = max(first_point[0], second_point[0])
    min_x = min(first_point[0], second_point[0])

    max_y = max(first_point[1], second_point[1])
    min_y = min(first_point[1], second_point[1])

    for x in range(min_x + 1, max_x):
        if (x, min_y + 1) in perimiter or (x, max_y + 1) in perimiter:
            return False

    for y in range(min_y + 1, max_y):
        if (min_x + 1, y) in perimiter or (max_x - 1, y) in perimiter:
            return False
    return True


def print_poly_grid(max_x: int, max_y: int, points: set[tuple]):
    for row in range(max_y + 1):
        print("")
        for column in range(max_x + 1):
            if (row, column) in points:
                print("X")
            else:
                print(".", end="")


def make_perimiter(tiles: list[tuple]) -> set[tuple]:
    points = set()
    for i in range(len(tiles)):
        if i < len(tiles) - 1:
            e = i + 1
        else:
            e = 0
        for x in range(
            min(tiles[i][0], tiles[e][0]), max(tiles[i][0], tiles[e][0] + 1)
        ):
            for y in range(
                min(tiles[i][1], tiles[e][1]), max(tiles[i][1], tiles[e][1] + 1)
            ):
                points.add((x, y))
    return points


def calc_new_max(
    first: tuple[int, int],
    second: tuple[int, int],
    perimiter: set[tuple],
    max_area: int,
) -> int:
    area = (abs(first[0] - second[0]) + 1) * (abs(first[1] - second[1]) + 1)
    if area <= max_area:
        return max_area
    if rect_in_poly(first, second, perimiter):
        print(f"New max:{area}")
        return area
    return max_area


def calc_area(
    first: tuple[int, int],
    second: tuple[int, int],
) -> int:
    return (abs(first[0] - second[0]) + 1) * (abs(first[1] - second[1]) + 1)


def parse_input(input_txt: str) -> list[tuple]:
    return [
        (int(x), int(y))
        for line in input_txt.splitlines()
        for x, y in [line.split(",")]
    ]
