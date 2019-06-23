from flask import Flask, request, render_template

app = Flask(__name__, template_folder='Templates')


@app.route('/')
def hello_world():
    return render_template('index.html')


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
