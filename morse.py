#!/usr/bin/env python
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

"""Morse.py - Translate English to Morse code, and vice versa.

Usage:
  morse.py [options] <msg>...

Options:
  -h, --help     Show this screen.
  -v, --version  Show the version.
"""


import re
from docopt import docopt
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
} # type: Dict[str, str]


morse = {v: k for k, v in eng.items()} # type: Dict[str, str]


def morsep(msg: str) -> bool:
    if msg[0][0] in ['.', '-', '/']:
        return True
    else:
        return False
        

def morse_to_eng(msg: str) -> str:
    out = "" # type: str
    msg = re.split("/| ", msg)
    msg = [e for e in msg if e]
    for char in msg:
        c = morse[char] # type: str
        out += c
    return("".join(out))


def eng_to_morse(msg: str) -> str:
    out = "" # type: str
    for char in msg:
        c = eng[char] # type: str
        out += "{} ".format(c)
    return("".join(out))


def decode(msg: str) -> str:
    "Main control flow."
    if morsep(msg) == True:
        return(morse_to_eng(msg))
    else:
        return(eng_to_morse(msg))


if __name__ == '__main__':
    args = docopt(__doc__, version = "Morse.py 0.1") # type: Dict
    out = decode(args['<msg>'][0]) # type: str
    print("{}".format(out))
