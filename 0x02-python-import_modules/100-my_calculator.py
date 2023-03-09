#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    sign = argv[2]
    opr_1 = int(argv[1])
    opr_2 = int(argv[3])

    dic = {"+": add, "-": sub, "*": mul, "/": div}

    if sign not in dic:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(opr_1, sign, opr_2, dic[sign](opr_1, opr_2)))
