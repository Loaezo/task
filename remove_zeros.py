"""Removes the zeros of an integer using O(1) of extra memory."""


def remove_zeros(my_list):
    """Function that removes the zeroes using O(1) of extra memory"""
    for number in my_list:
        if number == 0:
            my_list.remove(number)
    return my_list
