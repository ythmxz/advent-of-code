# Day 9: All in a Single Night (Part 2) https://adventofcode.com/2015/day/9#part2
from itertools import permutations


def find_worst_path(graph: dict, cities: set[str]) -> tuple[tuple[str, ...], float]:
    cities_list: list[str] = list(cities)
    worst_distance: float = 0.0
    worst_path: tuple[str, ...] = ()

    for permutation in permutations(cities_list):
        current_distance: float = 0
        is_valid: bool = True

        for i in range(len(permutation) - 1):
            u, v = permutation[i], permutation[i + 1]

            if v in graph[u]:
                current_distance += graph[u][v]
            else:
                is_valid = False

                break

        if is_valid and current_distance > worst_distance:
            worst_distance = current_distance
            worst_path = permutation

    return worst_path, worst_distance


distances: dict[str, dict[str, int]] = {}
cities: set[str] = set()

while True:
    try:
        line: str = input()
    except EOFError:
        break

    line = line.replace("to", "").replace("=", "")
    values: list[str] = line.strip().split()

    source: str = values[0]
    destination: str = values[1]
    weight: int = int(values[2])

    if source not in distances:
        distances[source] = {}

    if destination not in distances:
        distances[destination] = {}

    distances[source][destination] = weight
    distances[destination][source] = weight

    cities.add(source)
    cities.add(destination)

print(find_worst_path(distances, cities))
