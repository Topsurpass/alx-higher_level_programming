#!/usr/bin/python3


def multiple_returns(sentence):
    a = len(sentence)
    return a, sentence[0] if a > 0 else None
