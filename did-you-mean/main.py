#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from forms import QueryForm
import config
import json

# from wtforms.validators import DataRequired

# creating flask app
app = Flask(__name__)

# secret key for preventing CSRF
app.secret_key = config.SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def main():
    form = QueryForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('required')
            return render_template('index.html', form=form)
        else:
            results = ["Search Result", "Search Result2"]
            app.logger.info(results)
            return render_template('main.html', form=form, results=results)
    elif request.method == 'GET':
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run(host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)
