#!/usr/bin/python3
if __name__ == "__main__":
    """my calculator
    """
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    args_len = len(sys.argv) - 1

    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    sign = args[2]

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if sign not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    result = operators[args[2]](a, b)

    print("{} {} {} = {}".format(a, sign, b, result))
