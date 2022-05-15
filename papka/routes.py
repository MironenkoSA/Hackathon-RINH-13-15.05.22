from flask import Flask, render_template, url_for

from papka import app, db


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/avtoriz')
def avtoriz():
    return render_template('avtoriz.html')


@app.route('/regist')
def regist():
    return render_template('regist.html')


if __name__ == '__main__':
    app.run(debug=True)