#!/bin/env python3
import word_generator

v = ("a", "e", "i", "o", "u",
     "aa", "ee", "ii", "oo", "uu",
     "ae")
c = ("b", "s", "d", "f", "g", "h", "c", "l", "m", "n",
     "p", "r", "t", "i", "qu")
cc = ("bb", "ss", "dd", "ff", "cc", "ll", "mm", "n")
r = ("r", "l")
z = ("a", "us", "er", "um", "ii")


patterns = (
    (c, (r, ""), v, (c, cc), z),
)


rewrite_rules = {
    r"(?<=i)ii": "aa",
    r"mr": "br",
    r"nr": "t",
    r"hr": "fr",
    r"lr": "dr",
    r"rr": "r",
    r"sr": "s",
    r"sl": "s",
    r"dl": "dr",
    r"ml": "bl",
    r"nl": "t",
    r"hl": "fl",
    r"rl": "ll"
}


generator = word_generator.Generator(patterns, rewrite_rules)
print(generator.generate())
