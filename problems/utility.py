def read_strings():
    result = []
    while True:
        inp = input()
        if not inp:
            return result
        result.append(inp.strip())


def read_ints():
    return [int(i) for i in read_strings()]
