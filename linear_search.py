# This algorithm implements a linear search in a given list of numbers and returns the index of the target value.


def linear_search(list, target):
    """
    This function implements a linear search in a given list of numbers and returns the index of the target value.
    :param list: list of numbers
    :param target: target value
    :return: index of the target value
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify_search(value):
    """
    This function verifies if the linear search works correctly.
    :param value: target value
    """
    if value is not None:
        print("Target found at index: ", value)
    else:
        print("Target not found")


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers_list, 5)
verify_search(result)

result = linear_search(numbers_list, 20)
verify_search(result)
