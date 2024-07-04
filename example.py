#!/bin/env python3
import word_generator

v = ("a", "e", "i", "o", "u")
c = ("c", "m", "n", "p", "l", "s", "t")

patterns = (
    (c, v, v, c),
    ((c, ""), v, c, "a"),
)

generator = word_generator.Generator(patterns)
print(generator.generate())
