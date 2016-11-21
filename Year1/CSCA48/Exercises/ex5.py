def rsum(int_list):
    '''(list of int) -> int
    Given a list of integers, return the sum of all elements.
    REQ: List must contain at least one element
    REQ: List contains integers only
    >>> rsum([1, 2, 3])
    6
    >>> rsum([0, 0, 0])
    0
    >>> rsum([1])
    1
    '''
    # Base case
    if len(int_list) == 1:
        return int_list[0]

    # Summation of first value and all values following it
    else:
        return(int_list[0] + rsum(int_list[1:]))


def rmax(int_list):
    '''(list of int) -> int
    Given a list of integers, return the largest element
    REQ: List must contain at least one element
    REQ: List contains integers only
    >>> rmax([4])
    4
    >>> rmax([1, 2, 3, 4])
    4
    >>> rmax([4, 3, 2, 1])
    4
    >>> rmax([1, 1, 1, 1])
    1
    >>> rmax([-1, -2, -3, -4])
    -1
    '''
    # Base case
    if len(int_list) == 1:
        return int_list[0]
    # Return the largest element
    else:
        if int_list[0] >= rmax(int_list[1:]):
            return int_list[0]
        else:
            return rmax(int_list[1:])


def second_smallest(int_list, s=None, ss=None):
    '''(list of int, None or int, None or int) -> int
    Given a list of integer, return the second largest element
    REQ: List must contain at leat two elements
    REQ: List contains integers only
    >>> second_smallest([0, 0, 0])
    0
    >>> second_smallest([1, 2, 3, 4])
    2
    >>> second_smallest([4, 3, 2, 1, -1])
    1
    >>> second_smallest([4, 3, 2, 1])
    2
    >>> second_smallest([3, 1, 1])
    1
    >>> second_smallest([1, 1, 3])
    1
    >>> second_smallest([1, 1, 3, 3])
    1
    '''
    # Base case is one element list with two previously determined smallest
    # and second smallest
    if len(int_list) == 1:
        if(s <= int_list[0] <= ss):
            return int_list[0]
        elif (int_list[0] <= s):
            return s
        else:
            return ss

    else:
        if len(int_list) > 1 and s is None and ss is None:
            if(int_list[0] <= int_list[1]):
                return second_smallest(int_list[1:], int_list[0], int_list[1])
            else:
                return second_smallest(int_list[1:], int_list[1], int_list[0])
        else:
            # Re-write so it looks at one element at a time
            if (int_list[0] <= s):
                return second_smallest(int_list[1:], int_list[0], s)
            elif (s <= int_list[0] <= ss):
                return second_smallest(int_list[1:], s, int_list[0])
            else:
                return second_smallest(int_list[1:], s, ss)


def sum_max_min(int_list, s=None, b=None):
    '''(list of ints, None or int, None or int) -> int
    Given a list of integers, return the sum of the maximum and minimum value
    of the list
    REQ: list must contain at least one element
    >>> sum_max_min([4, 3, 2, 1, -1])
    3
    >>> sum_max_min([0])
    0
    >>> sum_max_min([1])
    2
    >>> sum_max_min([1, 1, 1])
    2
    >>> sum_max_min([3, 2, 1])
    4
    >>> sum_max_min([1, 0, 1, 0])
    1
    '''
    # Base case is an one element list with max and min already determined
    if len(int_list) == 1 and s is not None and b is not None:
        if (int_list[0] < s):
            return int_list[0] + b
        elif(b < int_list[0]):
            return s + int_list[0]
        else:
            return s + b

    else:
        if s is None and b is None:
            return sum_max_min(int_list[:], int_list[0], int_list[0])
        else:
            if int_list[0] < s:
                return sum_max_min(int_list[1:], int_list[0], b)
            elif b < int_list[0]:
                return sum_max_min(int_list[1:], s, int_list[0])
            else:
                return sum_max_min(int_list[1:], s, b)