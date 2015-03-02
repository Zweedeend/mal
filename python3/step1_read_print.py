# -*- encoding: utf-8 -*-
import reader
import printer


def READ(str_):
    return reader.read_str(str_)


def EVAL(ast):
    return ast


def PRINT(exp):
    return printer.pr_str(exp)


def rep(str_):
    return PRINT(EVAL(READ(str_)))


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