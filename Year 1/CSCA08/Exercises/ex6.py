def copy_me(i_list):
    '''(list) -> list
    Given a list, return a copy of the list with the apprioate changes to each
    element base on its type.
    REQ: List is not empty
    REQ: List contains only: Strings/Integers/Floats/Booleans/Lists
    >>> list1 = [ 'a', 1, 1.1, True, False, "false", ['a', b',c']]
    >>> copy_me(list1)
    ['A', 2, 2.1, False, True, 'FALSE', 'List']
    >>> print(list1)
    ['a', 1, 1.1, True, False, 'false', ['a', b',c']]
    '''
    r_list = i_list[:]
    for index in range(len(r_list)):
        # Element at index is a string, capitalize all of it
        if type(r_list[index]) is str:
            r_list[index] = r_list[index].upper()
        # Element at index is an integer or float, increase its value by 1
        elif type(r_list[index]) is int or type(r_list[index]) is float:
            r_list[index] += 1
        # Element at index is a boolean, negate its value
        elif type(r_list[index]) is bool:
            r_list[index] = not r_list[index]
        # Element at index is a list, change it to "List"
        else:
            r_list[index] = "List"
    return r_list


def mutate_me(i_list):
    '''(list) -> NoneType
    Given a list, return none and make the apprioate changes to each
    element base on its type.
    REQ: List is not empty
    REQ: List contains only: Strings/Integers/Floats/Booleans/Lists
    >>> list1 = [ 'a', 1, 1.1, True, False, 'false', ['a', b',c']]
    >>> mutate_me(list1)
    >>> print(list1)
    ['A', 2, 2.1, False, True, 'FALSE', 'List']
    '''
    # Loop through the list and make changes to the element based on its type
    for index in range(len(i_list)):
        # Element at index is a string, capitalize all of it
        if type(i_list[index]) is str:
            i_list[index] = i_list[index].upper()
        # Element at index is an integer or float, increase its value by 1
        elif type(i_list[index]) is int or type(i_list[index]) is float:
            i_list[index] += 1
        # Element at index is a boolean, negate its value
        elif type(i_list[index]) is bool:
            i_list[index] = not i_list[index]
        # Element at index is a list, change it to "List"
        else:
            i_list[index] = "List"
    return None
