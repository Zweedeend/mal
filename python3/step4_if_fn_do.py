#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import operator
import logging
from env import Env

import reader
import printer
from types import List, Symbol
from utils import grouper


logging.basicConfig(filename='log_step4.log', level=logging.DEBUG)


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
        head, *tail = ast
        if head == "def!":
            logging.debug("def! call: " + str(ast))
            symbol, assignment, *ignored = tail
            assigned = EVAL(assignment, env)
            env.set(symbol, assigned)
            return assigned
        if head == "let*":
            new_env = Env(outer=env)
            var_list, do_this, *ignored = tail
            for var, value in grouper(var_list, 2):
                value = EVAL(value, new_env)
                new_env.set(var, value)
            return EVAL(do_this, new_env)
        if head == "do":
            result = None
            for item in tail:
                result = EVAL(item, env)
            return result
        if head == "if":
            cond, if_true, if_false = tail
            if EVAL(cond, env) not in (None, False):
                return EVAL(if_true, env)
            return EVAL(if_false, env)
        if head == "fn*":
            params, body = tail
            new_env = Env(outer=env, binds=params, exprs=body)
            raise NotImplementedError
        # Default behavior
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