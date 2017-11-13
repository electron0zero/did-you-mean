#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from forms import QueryForm
from autocorrect import spell
from wordsegment import load, segment
from nltk import word_tokenize
import config
import json

# creating flask app
app = Flask(__name__)

# secret key for preventing CSRF
app.secret_key = config.SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def main():
    form = QueryForm()
    # wordsegment load function reads and parses the unigrams and bigrams data from disk.
    # Loading the data only needs to be done once.
    load()

    if request.method == 'POST':
        if form.validate() is False:
            flash('required')
            return render_template('index.html', form=form)
        else:
            result = segment_and_correct(form.search_key.data)
            return render_template('main.html', form=form, result=result)
    elif request.method == 'GET':
        return render_template('index.html', form=form)


def segment_and_correct(query):
    tokens = word_tokenize(query)
    final_text = ""
    for token in tokens:
        segments = segment(spell(token))
        if len(segments) > 1:
            for word in segments:
                final_text = final_text + spell(word) + " "
        else:
            final_text = final_text + segments[0] + " "
    return final_text


if __name__ == '__main__':
    app.debug = True
    app.run(host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)
