#!/usr/bin/python3

def safe_print_intger(value):

    """Safely print an integer value ith the {:d}
    formating

    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

    """else:
        return True
    """
