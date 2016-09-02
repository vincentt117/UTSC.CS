def rsum(int_list):
    '''(list of int and list of int) -> int
    Given a list of integers and lists of integers, return the sum of all
    elements.
    REQ: List must contain at least one element that is an integer
    REQ: List contains integers only
    >>> rsum([1, 2, 3])
    6
    >>> rsum([0, 0, 0])
    0
    >>> rsum([1])
    1
    >>> rsum([[1], [2, [3]], []])
    6
    '''
    # Base-cases
    if len(int_list) == 1:
        if isinstance(int_list[0], int):
            return int_list[0]
        elif isinstance(int_list[0], list):
            if int_list[0]:
                return (rsum(int_list[0]))
            # Treat empyt lists as zeros
            else:
                return 0

    else:
        if isinstance(int_list[0], int):
            return(int_list[0] + rsum(int_list[1:]))
        else:
            if int_list[0]:
                return(rsum(int_list[0]) + rsum(int_list[1:]))
            # Treat empyt lists as zeros
            else:
                return(0 + rsum(int_list[1:]))


def rmax(int_list):
    '''(list of int and list of int) -> int
    Given a list of integers and list of intergers, return the largest element
    REQ: List must contain at least one element that is an integer
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
    >>> rmax([[1], [2, [3]], []])
    3
    '''
    # Base case
    if len(int_list) == 1:
        if isinstance(int_list[0], int):
            return int_list[0]
        else:
            return rmax(int_list[0])
    # Return the largest element
    else:
        if isinstance(int_list[0], int):
            if int_list[0] >= rmax(int_list[1:]):
                return int_list[0]
            else:
                return rmax(int_list[1:])
        elif not int_list[0]:
            return rmax(int_list[1:])
        elif not int_list[1]:
            mod_list = int_list.pop(1)
            return rmax(int_list[0] + mod_list)
        else:
            return rmax(int_list[0] + int_list[1:])


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
    >>> second_smallest([1, [2, 3]])
    2
    >>> second_smallest([[1], [2, [3]], []])
    2
    '''
    # Base case being two values, select the larger of the two
    if len(int_list) == 1:
        if isinstance(int_list[0], int):
            if(s <= int_list[0] <= ss):
                return int_list[0]
            elif (int_list[0] <= s):
                return s
            else:
                return ss
        elif not int_list[0]:
            return ss
        else:
            return second_smallest(int_list[0], s, ss)

    else:
        if s is None and ss is None:
            if isinstance(int_list[0], int) and isinstance(int_list[1], int):
                if(int_list[0] <= int_list[1]):
                    return second_smallest(int_list[1:], int_list[0],
                                           int_list[1])
                else:
                    return second_smallest(int_list[1:], int_list[1],
                                           int_list[0])
            elif not int_list[0]:
                return second_smallest(int_list[1:], s, ss)
            elif isinstance(int_list[0], list):
                return second_smallest(int_list[0] + int_list[1:], s, ss)
            elif isinstance(int_list[1], list):
                mod_list = int_list[1:]
                mod_list.pop(0)
                return second_smallest(int_list[0:1] + int_list[1] + mod_list,
                                       s, ss)

        else:
            # Re-write so it looks at one element at a time
            if isinstance(int_list[0], int):
                if (int_list[0] <= s):
                    return second_smallest(int_list[1:], int_list[0], s)
                elif (s <= int_list[0] <= ss):
                    return second_smallest(int_list[1:], s, int_list[0])
                else:
                    return second_smallest(int_list[1:], s, ss)
            elif not int_list[0]:
                return second_smallest(int_list[1:], s, ss)
            else:
                return second_smallest(int_list[0] + int_list[1:], s, ss)


def sum_max_min(int_list, s=None, b=None):
    '''(list of int or list of int, None or int, None or int) -> int
    Given a list of integers and list of integers, return the sum of
    the maximum and minimum value of the list
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
    >>> sum_max_min([1, [2, 3]])
    4
    >>> sum_max_min([[1], [2, [3]], []])
    4
    '''
    # Base case
    if len(int_list) == 1:
        if s is not None and b is not None:
            if isinstance(int_list[0], int):
                if (int_list[0] < s):
                    return int_list[0] + b
                elif(b < int_list[0]):
                    return s + int_list[0]
                else:
                    return s + b
            elif not int_list[0]:
                return s + b
            else:
                return sum_max_min(int_list[0], s, b)

        else:
            if s is None and b is None:
                if isinstance(int_list[0], int):
                    return sum_max_min(int_list[:], int_list[0], int_list[0])
                elif not int_list[0]:
                    return sum_max_min(int_list[1:], None, None)
                else:
                    return sum_max_min(int_list[0], None, None)
    else:
        if s is None and b is None:
            if isinstance(int_list[0], int):
                return sum_max_min(int_list[:], int_list[0], int_list[0])
            elif not int_list[0]:
                return sum_max_min(int_list[1:], None, None)
            else:
                return sum_max_min(int_list[0] + int_list[1:], None, None)
        else:
            if isinstance(int_list[0], int):
                if int_list[0] < s:
                    return sum_max_min(int_list[1:], int_list[0], b)
                elif b < int_list[0]:
                    return sum_max_min(int_list[1:], s, int_list[0])
                else:
                    return sum_max_min(int_list[1:], s, b)
            elif not int_list[0]:
                return sum_max_min(int_list[1:], s, b)
            else:
                return sum_max_min(int_list[0] + int_list[1:], s, b)
