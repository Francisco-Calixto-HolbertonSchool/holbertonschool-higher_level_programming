#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for e in my_list:
            while i < x:
                print(e, end="")
                i += 1
                break
    except:
        pass
    print("")
    return i
