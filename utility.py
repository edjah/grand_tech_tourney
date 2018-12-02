def read_strings():
    result = []
    while True:
        try:
            inp = input()
        except Exception:
            return result

        result.append(inp.strip())


def read_ints():
    return [int(i) for i in read_strings()]
