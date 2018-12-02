from flask import Flask, url_for, render_template
app = Flask('frisson')


@app.route('/')
def index():
    return render_template('index.html')

