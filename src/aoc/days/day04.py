def solve_part1(input_txt: str) -> int:
    board = parse_input(input_txt)
    return sum(
        1
        for row in range(len(board))
        for col in range(len(board[row]))
        if board[row][col] == "@" and count_nearby_rolls(board, row, col) < 4
    )


def solve_part2(input_txt: str) -> int:
    removed_rolls = 0
    board = parse_input(input_txt)
    while True:
        result = remove_a_roll(board)
        if not result:
            return removed_rolls
        board = result
        removed_rolls += 1


def remove_a_roll(board: list[list[str]]) -> list[list[str]] | None:
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "@" and count_nearby_rolls(board, row, col) < 4:
                board[row][col] = "."
                return board
    return None


def parse_input(input_str: str) -> list[list[str]]:
    return [list(line) for line in input_str.splitlines()]


def count_nearby_rolls(board: list[list[str]], row: int, col: int) -> int:
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(
        1 for dr, dc in positions if char_at_position(board, dr + row, dc + col) == "@"
    )


def char_at_position(board: list[list[str]], row: int, col: int) -> str:
    if row < 0 or row >= len(board):
        return ""
    if col < 0 or col >= len(board[row]):
        return ""
    return board[row][col]
