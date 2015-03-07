#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import operator
import logging

from env import Env
import reader
import printer
from types import List, Symbol


logging.basicConfig(filename='log_step3.log', level=logging.DEBUG)


def READ(str_):
    return reader.read_str(str_)


def eval_ast(ast, env):
    if isinstance(ast, Symbol):  # a symbol
        return env.get(ast)
    if isinstance(ast, List):
        return [EVAL(item, env) for item in ast]
    return ast


def EVAL(ast, env):
    if isinstance(ast, List):
        if ast[0] == "def!":
            logging.debug("def! call: " + str(ast))
            symbol = ast[1]
            assignment = EVAL(ast[2], env)
            env.set(symbol, assignment)
            return assignment
        if ast[0] == "let*":
            new_env = Env(outer=env)
            var_list = iter(ast[1])
            var = value = None
            for i, item in enumerate(var_list):
                if i % 2 == 0:
                    var = item
                else:
                    value = EVAL(item, new_env)
                    new_env.set(var, value)
            return EVAL(ast[2], new_env)

        func, *args = eval_ast(ast, env)
        return func(*args)
    return eval_ast(ast, env)


def PRINT(exp):
    return printer.pr_str(exp)


repl_env = Env()

repl_env.set('+', operator.add)
repl_env.set('-', operator.sub)
repl_env.set('*', operator.mul)
repl_env.set('/', operator.floordiv)


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
        try:
            output = rep(value)
        except Exception as e:
            print(e)
            continue
        print(output)


if __name__ == '__main__':
    main()