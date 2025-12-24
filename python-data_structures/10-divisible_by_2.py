#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False depending on divisibility by 2"""
    result = []

    for n in my_list:
        result.append(n % 2 == 0)

    return result
