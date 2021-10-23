#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import flash, Flask, render_template, redirect, request, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'abc'

DB_FILE = 'votes.txt'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=['POST'])
def save():
    """"""
    gender = request.form.get('gender')

    if not gender:
        flash('Please select a gender.', 'error')
        return redirect(url_for('index'))
    else:
        with open(DB_FILE, 'a+') as f:
            f.write(f'{gender}\n')
        print(gender)
        flash('Thanks! Your vote has been saved!', 'info')
        return redirect(url_for('votes'))


@app.route("/votes", methods=['GET'])
def votes():
    """"""
    data = {'boy': 0, 'girl': 0}

    with open(DB_FILE) as f:
        contents = f.read()
        genders = contents.splitlines()
        for gender in genders:
            if gender == 'boy':
                data['boy'] += 1
            else:
                data['girl'] += 1

    return render_template("votes.html", data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_reloader=True)
