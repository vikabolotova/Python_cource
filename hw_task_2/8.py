elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]


def sort_key(e):
    return e[1]


print(sorted(elements, key = sort_key))