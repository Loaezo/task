"""Test tasks for Practicum's bootcamp"""


def missing_elements_0(list_1, list_2):
    """Returns the elements that are in the first list (list_1)
    but missing in the second (list_2)"""
    missing = []
    for element in list_1:
        if element not in list_2:
            missing.append(element)
    return missing


def missing_elements_1(list_1, list_2):
    """Returns the elements that are in the first list (list_1)
    but missing in the second (list_2). More optimized solution"""
    set2 = set(list_2)
    return (element for element in list_1 if element not in set2)
