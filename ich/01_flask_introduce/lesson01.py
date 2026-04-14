from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/user/<int:user_id>')
def show_user_profile_by_id(user_id):
    print(user_id, type(user_id))
    return f'User with id {user_id}'

@app.route('/files/<path:filepath>')
def show_file(filepath):
    print(filepath, type(filepath))
    return f'File located at: {filepath}'

@app.route('/customer/<uuid:user_id>')  # 32 символа в 16-чной кодировке fmt: 8-4-4-4-12
def show_user_profile_by_uuid(user_id):
    print(user_id, type(user_id))
    return f'User with UUID: {user_id}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
