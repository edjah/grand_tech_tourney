def read_strings():
    result = []
    while True:
        try:
            inp = input()
        except Exception as e:
            return result

        result.append(inp.strip())


def read_ints():
    return [int(i) for i in read_strings()]
