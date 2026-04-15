from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/user/<name>')
def greeting_user(name):
    return f'Hello {name}!'

@app.route('/multiple/<int:two_mult>')
def multiplied(two_mult):
    return f'Parameter {two_mult} multiplied by two equal: {two_mult * 2}'

@app.route('/squaring/<float:digit>')
def squaring(digit):
    return f'Parameter {digit} squared by {digit ** 2}'

@app.route('/reverse/<path:text>')
def reverse_text(text):
    return f'{text} reversed is {text[::-1]}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
