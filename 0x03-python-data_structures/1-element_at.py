#!/usr/bin/python3
def element_at(my_list, idx):

    size = len(my_list)
    Error = "None"

    if idx < 0 or idx >= size:
        return Error
    else:
        return(my_list[idx])
