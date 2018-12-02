import glob
import os
import secrets
from flask import Flask, render_template, request, jsonify
from subprocess import Popen, PIPE

import redis
import json

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
)


app = Flask(__name__)
app.secret_key = '0dd93afabcb285da44449b65664c87ee9a1ecaef27eb27c2'

supported_languages = {'c', 'cpp', 'py', 'js', 'ml'}
num_problems = 1


def run(command, stdin=None):
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate(input=stdin)
    return (
        process.returncode,
        stdout.decode('utf-8').strip(),
        stderr.decode('utf-8').strip()
    )


def check_code(problem, executable):
    test_files = sorted(glob.glob(f'problems/problem{problem}/tests/*'))
    assert len(test_files) % 2 == 0, 'Some test is missing a result'

    for i in range(0, len(test_files), 2):
        exp_file = test_files[i]
        inp_file = test_files[i + 1]
        assert inp_file.endswith('.inp'), inp_file
        assert exp_file.endswith('.exp'), exp_file
        assert inp_file[:-4] == exp_file[:-4]

        with open(exp_file, 'r') as fp:
            exp = fp.read().rstrip()

        with open(inp_file, 'rb') as fp:
            retcode, stdout, stderr = run(executable, stdin=fp.read())
            if retcode != 0:
                print(stdout, stderr)
                return ('Exception', 1 + i // 2, stderr, exp)

            if stdout != exp:
                return ('Incorrect', 1 + i // 2, stdout, exp)

    return ('OK', None, None, None)


@app.route('/check', methods=['POST'])
def check():
    problem = request.form.get('problem')
    code = request.form.get('code')
    file_ext = request.form.get('file_ext')

    # validating input
    if not problem or not code or not file_ext or not problem.isdigit():
        return jsonify({'error': 'Bad request'}), 400
    if file_ext not in supported_languages:
        return jsonify({'error': 'Language not supported'}), 400
    if int(problem) not in range(1, num_problems + 1):
        return jsonify({'error': 'Invalid problem'}), 400
    problem = f'{int(problem):02}'

    # make a temporary directory to store the user's code
    tmp_dir = '/tmp/' + secrets.token_hex(16)
    try:
        os.makedirs(tmp_dir)
        run(f'cp -r problems/problem{problem}/* {tmp_dir}/')

        with open(tmp_dir + f'/problem{problem}.{file_ext}', 'w') as fp:
            fp.write(code)

        if file_ext == 'c' or file_ext == 'cpp':
            retcode, stdout, stderr = run(f'make {tmp_dir}/problem{problem}')
            if retcode != 0:
                return jsonify({'error': 'compile', 'stderr': stderr})
            executable = f'{tmp_dir}/problem{problem}'
        elif file_ext == 'py':
            executable = f'python3 {tmp_dir}/problem{problem}.py'
        elif file_ext == 'js':
            executable = f'node {tmp_dir}/problem{problem}.js'
        elif file_ext == 'ml':
            executable = f'ocaml {tmp_dir}/problem{problem}.ml'
        else:
            raise Exception(f'Unimplemented language: {file_ext}')

        status, test_num, got, expected = check_code(problem, executable)
        return jsonify({
            'test_num': test_num,
            'status': status,
            'expected': expected,
            'got': got
        })

    finally:
        run(f'rm -rf {tmp_dir}')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/teams', methods=['GET'])
def teams():
    s = r.get('teams')

    if s is not None:
        parsed = json.loads(s)
    else:
        parsed = []

    return jsonify(parsed)

    # [
    #     {
    #         'name': 'sample',
    #         'score': 5,
    #         'handicaps': [],
    #     },
    #     {
    #         'name': 'sample',
    #         'score': 10,
    #         'handicaps': ['shots shots', 'shots']
    #     }
    # ]

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
