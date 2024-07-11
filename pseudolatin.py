#!/bin/env python3
import word_generator

v = ("a", "e", "i", "o", "u",
     "aa", "ee", "ii", "oo", "uu")
c = ("b", "s", "d", "f", "g", "h", "c", "l", "m", "n",
     "p", "r", "t", "v", "i", "qu")
cc = ("bb", "ss", "dd", "ff", "gg", "cc", "ll", "mm", "n")

patterns = (
    ((c, ""), v, ("s", "m", "l"), (c, cc), ("as", "us", "um", "ii")),
)

generator = word_generator.Generator(patterns)
print(generator.generate())
