# Day 5: Doesn't He Have Intern-Elves For This? https://adventofcode.com/2015/day/5
def has_three_vowels(string: str) -> bool:
    vowel_count: int = 0

    for s in string:
        if s in VOWELS:
            vowel_count += 1

            if vowel_count >= 3:
                return True

    return False


def has_double_letter(string: str) -> bool:
    for s in string:
        if s + s in string:
            return True

    return False


def has_substrings(string: str) -> bool:
    for s in SUBSTRINGS:
        if s in string:
            return True

    return False


VOWELS: list[str] = ["a", "e", "i", "o", "u"]
SUBSTRINGS: list[str] = ["ab", "cd", "pq", "xy"]

nice_strings: int = 0

while True:
    try:
        line: str = input().strip()
    except EOFError:
        break

    if has_three_vowels(line) and has_double_letter(line) and not has_substrings(line):
        nice_strings += 1

print(nice_strings)
