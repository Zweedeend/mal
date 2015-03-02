# -*- encoding: utf-8 -*-
import operator
import logging
import reader
import printer
from types import List, Symbol


logging.basicConfig(filename='step2.log', level=logging.DEBUG)


def READ(str_):
    return reader.read_str(str_)


def eval_ast(ast, env):
    if isinstance(ast, Symbol) and ast in env:  # a symbol
        return env[ast]
    if isinstance(ast, List):
        return [eval_ast(item, env) for item in ast]
    return ast


def EVAL(ast, env):
    if isinstance(ast, list):
        func, *args = ast
        if func in env:
            func = env[func]
            return func(*args)
    return eval_ast(ast, env)


def PRINT(exp):
    return printer.pr_str(exp)


repl_env = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def rep(text):
    return PRINT(EVAL(READ(text), repl_env))


def main():
    while True:
        try:
            value = input("mal> ")
        except EOFError:
            print("Goodbye!")
            break
        if not value:
            continue
        output = rep(value)
        print(output)


if __name__ == '__main__':
    main()