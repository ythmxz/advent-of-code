from itertools import permutations

def find_best_path(graph: dict, cities: set[str]) -> tuple[tuple[str, ...], float]:
    cities_list: list[str] = list(cities)
    best_distance: float = float('inf')
    best_path: tuple[str, ...] = ()

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

        if is_valid and current_distance < best_distance:
            best_distance = current_distance
            best_path = permutation

    return best_path, best_distance


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

print(find_best_path(distances, cities))
