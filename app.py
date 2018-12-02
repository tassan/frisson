from flask import Flask
app = Flask('frisson')


@app.route('/')
def main():
    return 'Welcome to the frisson'


@app.route('/hello/')
def hello():
    return 'Hello World!'


@app.route('/hello_user/<username>')
def hello_user(username):
    return 'Hello %s' % username
