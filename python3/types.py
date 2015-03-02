# -*- encoding: utf-8 -*-
from printer import pr_str


class List(list):
    def __str__(self):
        return "(" + " ".join(pr_str(item) for item in self) + ")"


class Symbol(str):
    pass


class Int(int):
    pass


class String(str):
    def __str__(self):
        return '"' + self + '"'



