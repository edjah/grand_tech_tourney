import os
import subprocess
import random
from secrets import token_hex


def run(*args, **kwargs):
    return subprocess.call(*args, **kwargs, shell=True)


def arr_to_file(a, file):
    with open(file, 'w') as fp:
        fp.write('\n'.join(str(i) for i in a) + '\n')


def setup_test_dir(prob_num):
    # making the directory
    try:
        os.makedirs(f'problem{prob_num:02}/tests')
    except Exception:
        pass

    # copying files over
    run(f'cp base.md problem{prob_num:02}/problem{prob_num:02}_statement.md')
    run(f'cp base.py problem{prob_num:02}/problem{prob_num:02}.py')
    run(f'cp base.c problem{prob_num:02}/problem{prob_num:02}.c')
    run(f'cp base.cpp problem{prob_num:02}/problem{prob_num:02}.cpp')
    run(f'cp base.ml problem{prob_num:02}/problem{prob_num:02}.ml')
    run(f'cp base.js problem{prob_num:02}/problem{prob_num:02}.js')
    run(f'cp utility.h Makefile problem{prob_num:02}/')
    run(f'cp utility.py Makefile problem{prob_num:02}/')


# custom code for generating tests
def make_problem_1_tests():
    test_dir = f'problem01/tests/'
    if not os.path.exists(test_dir):
        setup_test_dir(1)

    arr_to_file([1, 2, 3, 4, 5, 1], test_dir + f'01.inp')
    arr_to_file([0], test_dir + f'01.exp')

    arr_to_file([1, 2, 3, 4, 5, 5], test_dir + f'02.inp')
    arr_to_file([4], test_dir + f'02.exp')

    arr_to_file([1, 2, 4, 5, 3], test_dir + f'03.inp')
    arr_to_file([-1], test_dir + f'03.exp')

    arr_to_file([1873], test_dir + f'04.inp')
    arr_to_file([-1], test_dir + f'04.exp')

    # automated tests
    for i in range(5, 21):
        sz = random.randint(1, 2 ** i)
        a = sorted(set(random.randint(0, 10 ** 6) for i in range(sz)))

        if random.randint(0, 1):
            idx = random.randint(0, 10 ** 6)
        else:
            idx = a[random.randint(0, len(a) - 1)]

        try:
            res_idx = a.index(idx)
        except ValueError:
            res_idx = -1

        a.append(idx)
        arr_to_file(a, test_dir + f'{i:02}.inp')
        arr_to_file([res_idx], test_dir + f'{i:02}.exp')


def make_problem_2_tests():
    test_dir = f'problem02/tests/'
    if not os.path.exists(test_dir):
        setup_test_dir(2)

    for i in range(10):
        a = token_hex(i)
        b = token_hex(i) + token_hex(1)[0]

        arr_to_file([a], test_dir + f'{2 * i:02}.inp')
        arr_to_file([a[::-1]], test_dir + f'{2 * i:02}.exp')
        arr_to_file([b], test_dir + f'{2 * i + 1:02}.inp')
        arr_to_file([b[::-1]], test_dir + f'{2 * i + 1:02}.exp')


def make_problem_3_tests():
    test_dir = f'problem03/tests/'
    if not os.path.exists(test_dir):
        setup_test_dir(3)

    for n in range(1, 10):
        a = [random.randint(-10000, 10000) for _ in range(n)]
        arr_to_file(a, test_dir + f'{n:02}.inp')
        arr_to_file(sorted(a), test_dir + f'{n:02}.exp')

    for n in range(10, 20):
        sz = random.randint(10, 100000)
        a = [random.randint(-10000, 10000) for _ in range(sz)]
        arr_to_file(a, test_dir + f'{n:02}.inp')
        arr_to_file(sorted(a), test_dir + f'{n:02}.exp')


def make_problem_4_tests():
    test_dir = f'problem04/tests/'
    # if not os.path.exists(test_dir):
    #     setup_test_dir(4)

    def two_sum(a, target):
        from collections import Counter
        c = Counter(a)

        for x in a:
            if c.get(target - x, 0) >= 1:
                if target - x == x and c.get(target - x, 0) >= 2:
                    return 1
                elif target - x != x:
                    return 1

        return 0

    for n in range(1, 21):
        sz = random.randint(10, 100000)

        a = [random.randint(-10000, 10000) for _ in range(sz)]
        seen = set()
        aa = []
        for i in a:
            if i in seen:
                continue
            aa.append(i)
            seen.add(i)
        a = aa

        b = random.randint(-100000, 100000)
        if random.random() < 0.2:
            x = random.randint(0, len(a) - 1)
            y = random.randint(0, len(a) - 1)
            b = a[x] + a[y]

        arr_to_file(a + [b], test_dir + f'{n:02}.inp')
        arr_to_file([two_sum(a, b)], test_dir + f'{n:02}.exp')


# make_problem_1_tests()
# make_problem_2_tests()
# make_problem_3_tests()
make_problem_4_tests()
