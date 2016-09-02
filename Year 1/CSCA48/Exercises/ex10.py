def radix_sort(int_list, base=10):
    '''(list of ints, int) -> list of ints
    Return a list with the elements of int_list is ascending order
    REQ: All elements in int_list are positive integers
    >>> radix_sort([0])
    [0]
    >>> radix_sort([1, 2, 3])
    [1, 2, 3]
    >>> radix_sort([3, 2, 1])
    [1, 2, 3]
    >>> radix_sort([1, 111, 11, 11111])
    [1, 11, 111, 11111]
    >>> radix_sort([240, 28, 500000000, 18, 140, 2])
    [2, 18, 28, 140, 240, 500000000]
    '''
    # Main bin
    bin_list = int_list[:]
    # Form the bins
    dig_bin = {0: [], 1: [], 2: [], 3: [], 4: [],
               5: [], 6: [], 7: [], 8: [], 9: []}
    # Place elements into bins based on their digit
    all_digits_accounted_for = True
    for i in bin_list:
        if i*10 <= base:
            dig_bin[0].append(i)
        else:
            all_digits_accounted_for = False
            dig_bin[i % base // (base / 10)].append(i)
    ret_list = []
    for i in range(0, 10):
        ret_list += dig_bin[i]
    if all_digits_accounted_for:
        return ret_list
    else:
        return radix_sort(ret_list, base*10)
