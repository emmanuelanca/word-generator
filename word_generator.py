#!/bin/env python3
import random
import re


class Generator:
    def __init__(self, patterns, rewrite_rules):
        self.patterns = patterns
        self.rewrite_rules = rewrite_rules

    def generate(self):
        word = ""
        pattern = random.choice(self.patterns)
        for expression in pattern:
            while type(expression) is not str:
                expression = random.choice(expression)
            word = word + expression
        for pattern, replacement in self.rewrite_rules.items():
            word = re.sub(pattern, replacement, word)
        return word
