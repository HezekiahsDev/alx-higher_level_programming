#!/usr/bin/python3

# this program imports module 'add' from a add_0

if __name__ == "__main__":

    from add_0 import add

    a = 1
    b = 2
    c = add(a, b)

    print("{:d} + {:d} = {:d}", a, b, c)
