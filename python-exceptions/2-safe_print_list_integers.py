#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0

    while count < x:
        try:
            value = my_list[count]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed += 1
        except Exception:
            raise
        count += 1

    print()
    return printed
