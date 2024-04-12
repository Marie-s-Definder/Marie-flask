from flask import Flask, request

app = Flask(__name__)

@app.route('/Recognition', methods=['POST'])
def Recognition():
    data = request.json
    url = data.get('url')
    data = data.get('data')
    print(url)

    print(len(data))
    return f'Hello, {url}!'


if __name__ == '__main__':
    app.run(debug=True)