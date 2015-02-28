# -*- encoding: utf-8 -*-

def READ(value):
    return value


def EVAL(value):
    return value


def PRINT(value):
    return value


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
        output = rep(value)
        print(output)


if __name__ == '__main__':
    main()