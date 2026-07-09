from itertools import groupby


value: str = input().strip()
new_value: str = ""

value_groups: list[str] = []

count: int = 0
char: str = ""

for i in range(40):
    new_value = ""
    value_groups = ["".join(group) for _, group in groupby(value)]

    for g in value_groups:
        count = len(g)
        char = g[0]

        new_value += f"{count}{char}"

    value = new_value

print(len(value))
