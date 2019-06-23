from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/address', methods=['POST'])
def set_address():
    if request.method == 'POST':
        data = request.form.get('data')
        print(data)
        with open('data.txt', 'a') as f:
            f.write(data)
            f.write('/n')
        return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
