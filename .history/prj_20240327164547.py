from flask import Flask, request

app = Flask(__name__)

@app.route('/Recognition', methods=['GET'])
def Recognition():
    path = request.args.get('url')
    data = request.args.get('data')
    print(path)
    print(data)
    return f'Hello, {path}!'


if __name__ == '__main__':
    app.run(debug=True)