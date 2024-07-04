#!/bin/env python3
import random


class Generator:
    def __init__(self, patterns):
        self.patterns = patterns

    def generate(self):
        word = ""
        pattern = random.choice(self.patterns)
        for expression in pattern:
            while type(expression) is not str:
                expression = random.choice(expression)
            word = word + expression
        return word
