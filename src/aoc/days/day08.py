from math import dist, prod


def solve_part1(input_txt: str) -> int:
    CONNECTIONS = 1000
    points = parse_points(input_txt)
    circuits = {}
    points_to_circuits = {}
    ckey = 0
    for point in points:
        c = [point]
        points_to_circuits[point] = len(circuits)
        circuits[ckey] = c
        ckey += 1
    distances = sorted(calculate_distances(points))
    for i in range(CONNECTIONS):
        if i >= len(distances):
            raise IndexError(
                "Expected length of distances to be greated than number of desired connections"
            )
        _, start, end = distances[i]
        start_circuit = points_to_circuits[start]
        end_circuit = points_to_circuits[end]
        if start_circuit == end_circuit:
            continue
        circuits[start_circuit].extend(circuits[end_circuit])
        del circuits[end_circuit]
        for point, circuit in points_to_circuits.items():
            if circuit == end_circuit:
                points_to_circuits[point] = start_circuit
    three_longest = sorted(circuits.values(), key=len, reverse=True)[:3]
    # print(three_longest)
    return prod(map(len, three_longest))


def solve_part2(input_txt: str) -> int:
    points = parse_points(input_txt)
    circuits = {}
    points_to_circuits = {}
    ckey = 0
    for point in points:
        c = [point]
        points_to_circuits[point] = len(circuits)
        circuits[ckey] = c
        ckey += 1
    distances = sorted(calculate_distances(points))
    for i in range(len(distances)):
        _, start, end = distances[i]
        start_circuit = points_to_circuits[start]
        end_circuit = points_to_circuits[end]
        if start_circuit == end_circuit:
            continue
        circuits[start_circuit].extend(circuits[end_circuit])
        del circuits[end_circuit]
        if len(circuits) == 1:
            return start[0] * end[0]
        for point, circuit in points_to_circuits.items():
            if circuit == end_circuit:
                points_to_circuits[point] = start_circuit
    return 0


def parse_points(input_txt: str) -> list[tuple]:
    points = [
        tuple(int(coord) for coord in line.split(","))
        for line in input_txt.splitlines()
    ]
    return points


def calculate_distances(points: list[tuple]) -> list[tuple]:
    distance_pairs = []
    for i, starting_point in enumerate(points):
        for ending_point in points[i + 1 :]:
            if starting_point == ending_point:
                continue
            distance = dist(starting_point, ending_point)
            distance_pairs.append((distance, starting_point, ending_point))
    return distance_pairs
