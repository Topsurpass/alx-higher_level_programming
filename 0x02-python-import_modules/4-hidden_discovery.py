#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for i in dir(calculator_1):
        if i.startswith("__"):
            continue
        else:
            print(i)
