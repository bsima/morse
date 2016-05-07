#!/usr/bin/env python3
#
# Morse.py - A morse code interpreter.
#
# A friend of mine likes to send me messages in Morse code
# sometimes. He's a little weird. He thinks I'm really good at Morse
# code. Actually, I can just do some Python.
#
# Author: Ben Sima <bensima@gmail.com>
# Date: 2015-07-06
# License: MIT
#


import re
import argparse
from typing import Dict


eng = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    " " : "/",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "," : ",",
    "." : ".",
    "!" : "!",
    "?" : "?",
} # type: Dict[str, str]


morse = {v: k for k, v in eng.items()} # type: Dict[str, str]


class InvalidMorseLetter(Exception):
    "Handle errors when processing Morse Code."
    pass


class InvalidEnglishLetter(Exception):
    "Handle errors when processing English."
    pass


def morsep(msg: str) -> bool:
    "Predicate for detecting Morse Code."
    return msg[0][0] in ['.', '-', '/']


def morse_to_eng(msg: str) -> str:
    """Translate Morse code to English.

    Will raise an InvalidMorseLetter if an error during
    the translation occurs."""
    split_msg = re.split(" ", msg) # type: list
    filtered_msg = [e for e in split_msg if e] # type: list
    try:
        return ''.join("{}".format(morse[char]) for char in filtered_msg)
    except KeyError:
        raise InvalidMorseLetter

def eng_to_morse(msg: str) -> str:
    """Translate English into Morse Code.

    Will rais an InvalidEnglishLetter if an error during
    the translation occurs."""
    try:
        return ''.join("{} ".format(eng[char]) for char in msg)
    except KeyError:
        raise InvalidEnglishLetter


def decode(msg: str) -> str:
    "Main control flow."
    lower_msg = msg.lower()
    if morsep(lower_msg) == True:
        return morse_to_eng(lower_msg)
    else:
        return eng_to_morse(lower_msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate English to Morse code, and vice versa.')
    parser.add_argument('-v', '--version', help='Show the version.', action='version',
            version='Morse 0.1')
    parser.add_argument('msg', type=str, nargs=1,
                        help="""The message to be decoded.
                        Input type will be automatically detected and converted.
                        Must be wrapped in quotes.""")

    args = parser.parse_args()
    out = decode(args.msg[0]) # type: str
    print("{}".format(out))
