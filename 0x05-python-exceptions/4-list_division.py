#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_lenght):
    a = my_list_1
    b = my_list_2
    llen = list_lenght
    div_list = []

    for i in range(llen):
        try:
            div = a[i] / b[i]

        except (ValueError, TypeError):
            print("Wrong type")
            div = 0

        except ZeroDivisionError:
            print("division by 0")
            div = 0

        except IndexError:
            print("out of range")
            div = 0

        finally:
            div_list.append(div)

        return div_list
