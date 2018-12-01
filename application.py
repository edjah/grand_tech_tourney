import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = '0dd93afabcb285da44449b65664c87ee9a1ecaef27eb27c2'

supported_languages = {'C', 'C++', 'Python', 'JavaScript', 'OCaml'}


def check_c_cpp(code):
    pass


@app.route('/check', methods=['POST'])
def check():
    code = request.form.get('code')
    language = request.form.get('language')

    if not code:
        return jsonify({'error': 'File is empty'}), 400
    if language not in supported_languages:
        return jsonify({'error': 'Language not supported'}), 400

    return jsonify({'status': 'Correct solution'})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
