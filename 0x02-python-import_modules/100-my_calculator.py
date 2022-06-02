#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    #choose operation

    a, opp, b = sys.argv[1:]

    if sys.argv[2] == '+':
        func = add
    elif sys.argv[2] == '-':
        func = sub
    elif sys.argv[2] == '*':
        func = mul
    else:
        sys.argv[2] == '/'
        func = div

    #perform calculation
print("{} {} {} = {:d}".format(a, opp, b, func(int(a), int(b))))
