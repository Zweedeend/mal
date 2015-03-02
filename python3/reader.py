# -*- encoding: utf-8 -*-
import logging
import re
from types import List, Int, String


class Reader:
    def __init__(self, tokens):
        self.position = 0
        self.tokens = tokens

    def next(self):
        """returns the tokens at the current position and increments the position."""
        self.position += 1
        peek = self.peek()
        return peek

    def peek(self):
        """ just returns the token at the current position."""
        return self.tokens[self.position]


def read_str(value):
    logging.debug("read_str({value!r})".format(value=value))
    tokens = tokenize(value)
    logging.debug("tokens: " + repr(tokens))
    reader = Reader(tokens)
    return read_form(reader)


def tokenize(value):
    return re.findall(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)""", value)


def read_form(reader):
    token = reader.peek()
    if token == "(":
        return read_list(reader)
    else:
        return read_atom(reader)


def read_list(reader):
    results = List()
    while True:
        token = reader.next()
        if token == ")":
            return results
        results.append(read_form(reader))


def read_atom(reader):
    token = reader.peek()
    if token.isdigit():
        return Int(token)
    if token.startswith('"') and token.endswith('"'):
        return String(token[1:-1])  # strip the quotes
    return str(token)


