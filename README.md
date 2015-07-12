# Morse

A simple morse code interpreter. Currently a naive, lookup-table implementation. I use [mypy](http://mypy-lang.org/) for type checking, 'cause it's fun..

## Setup

Make sure you have Python 3.4, pip, and virtualenv. Then:

    $ git clone git@github.com:bsima/morse.git && cd morse
    $ virtualenv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python morse.py -h # Show usage information

## Example

Morse will automatically detect the input method, just be sure to wrap `<msg>` in quotes:

    (env)$ python morse.py "github"
    --. .. - .... ..- -...
    (env)$ python morse.py "--. .. - .... ..- -..."
    github

## Todo:

Implement the [Boyer-Moore algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm) (or similar).


