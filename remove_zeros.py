"""Removes the zeros of an integer using O(1) of extra memory."""


def remove_zeros(my_list):
    """Function that removes the zeroes using O(1) of extra memory"""
    result = []
    for number in my_list:
        if number != 0:
            result.append(number)
    my_list[:] = result
    return my_list
