# -*- encoding: utf-8 -*-
import reader, printer

def READ(value):
    return reader.read_str(value)


def EVAL(value):
    return value


def PRINT(value):
    return printer.pr_str(value)


def rep(value):
    read = READ(value)
    eval_ = EVAL(read)
    print_ = PRINT(eval_)
    return print_


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