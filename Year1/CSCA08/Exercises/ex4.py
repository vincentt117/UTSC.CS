def insert(listA, listB, index):
    '''(list, list, int) -> list
    Given 2 lists and an integer index, return the first list with the second
    list inserted at the given index
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'
    '''
    # Splices listA into three components and inserts list B in between
    # set listA as this newly created list and return
    return listA[0:index] + listB + listA[index:]


def up_to_first(listA, reference):
    '''(list, obj) -> list
    Given a list and an object, return the list up to the first occurance of
    that object. In the event where the element does not exist in the list
    return the entire list
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    >>> up_to_first("abc", "b")
    'a'
    >>> up_to_first("abc", "x")
    'abc'
    '''
    # Scenarios in which the reference does exist in the list
    if(listA.count(reference) >= 1):
        return listA[0:listA.index(reference)]
    # Scenarios in which the refernce does not exist in the list
    else:
        return listA


def cut_list(listA, index):
    '''(list, int) -> list
    Given a list and an integer reference, return the list with the elements
    before and after the index swapped.
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    # Splices the list into two components and returns the list with
    # elements in the following order: item index to final item, item index,
    # and item 0 to item index
    return listA[index+1:] + listA[index:index+1] + listA[:index]
