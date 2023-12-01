#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    result = 0
    args = sys.argv

    for i in range(len(args) - 1):
        result = result + int(args[i + 1])
    print("{}".format(result))
