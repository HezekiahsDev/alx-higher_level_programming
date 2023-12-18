#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    rExc = "Too far"
    mgcPow = a ** b
    mgcAdd = a + b

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception(rExc)
            else:
                result += mgcPow / i

        except Exception:
            result = mgcAdd
            break
    return result
