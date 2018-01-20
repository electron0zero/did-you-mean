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
            result = segment_and_correct(form.search_key.data, spelling=True, segmenting=True)
            return render_template('main.html', form=form, result=result)
    elif request.method == 'GET':
        return render_template('index.html', form=form)


def segment_and_correct(payload, spelling, segmenting):
    tokens = word_tokenize(payload)

    final_tokens = []

    if (segmenting and spelling):
        segmented = segment_tokens(tokens)
        final_tokens = spell_tokens(segmented)
    if (segment and not spelling):
        final_tokens = segment_tokens(tokens)
    if (spelling and not segmenting):
        final_tokens = spell_tokens(tokens)
    final_text = " ".join(final_tokens)
    # print("is it same: ", is_it_equal(payload, final_text))
    return final_text

def segment_tokens(tokens):
    segmented_tokens = []
    for token in tokens:
        segments = segment(token)
        segmented_tokens.extend(segments)
    return segmented_tokens

def spell_tokens(tokens):
    spelled_tokens = []
    for token in tokens:
        spelled = spell(token)
        spelled_tokens.append(spelled)
    return spelled_tokens

def is_it_equal(first, second):
    try:
       return first.lower() == second.lower()
    except AttributeError:
       return first == second


if __name__ == '__main__':
    app.debug = True
    app.run(host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)
