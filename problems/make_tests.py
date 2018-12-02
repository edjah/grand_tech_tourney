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


# make_problem_1_tests()
make_problem_2_tests()
