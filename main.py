from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    print('I am inside hello world')
    return 'Hello World! CD'


@app.route('/echo/<name>')
def echo(name):
    print(f'This is in the url: new-{name}')
    val = {'new-name': name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=800, debug=True)