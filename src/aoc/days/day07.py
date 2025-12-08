from collections import defaultdict


def solve_part1(input_txt: str) -> int:
    width, start_pos, splits = parse_board(input_txt)
    beam_positions = {start_pos}
    split_count = 0
    for row in splits:
        next_beam_positions = beam_positions.copy()
        for splitter in row:
            if splitter in beam_positions:
                split_count += 1
                next_beam_positions.remove(splitter)
                if splitter > 0:
                    next_beam_positions.add(splitter - 1)
                if splitter < width:
                    next_beam_positions.add(splitter + 1)
        beam_positions = next_beam_positions.copy()
    return split_count


def solve_part2(input_txt: str) -> int:
    graph = graph_from_board(*parse_board(input_txt))
    return count_paths(0, graph, {})


def parse_board(input_txt: str) -> tuple[int, int, list[list[int]]]:
    lines = input_txt.splitlines()
    width = len(lines[0])
    start_pos = lines[0].find("S")
    splits = []
    for line in lines[1:]:
        splits.append([i for i, c in enumerate(line) if c == "^"])
    return width, start_pos, splits


def graph_from_board(
    width: int, start_pos: int, rows: list[list[int]]
) -> list[list[int]]:
    graph = []
    graph.append([])
    beam_positions = {start_pos}
    beam_parents = defaultdict(list)
    beam_parents[start_pos] = [0]
    for row in rows:
        next_beam_positions = beam_positions.copy()
        for splitter in row:
            if splitter in beam_positions:
                for parent in beam_parents[splitter]:
                    graph[parent].append(len(graph))
                graph.append([])
                if splitter > 0:
                    next_beam_positions.add(splitter - 1)
                    beam_parents[splitter - 1].append(len(graph) - 1)
                if splitter < width:
                    next_beam_positions.add(splitter + 1)
                    beam_parents[splitter + 1].append(len(graph) - 1)
                next_beam_positions.remove(splitter)
                del beam_parents[splitter]
        beam_positions = next_beam_positions.copy()
    for pos in beam_positions:
        for parent in beam_parents[pos]:
            graph[parent].append(len(graph))
        graph.append([])
    # print(graph)
    return graph


def count_paths(node: int, children: list[list[int]], memo: dict) -> int:
    if node in memo:
        return memo[node]
    if len(children[node]) == 0:
        memo[node] = 1
        return 1
    total = sum(count_paths(child, children, memo) for child in children[node])
    memo[node] = total
    return total
