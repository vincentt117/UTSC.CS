def greeting(name):
    '''
    (str) -> str
    Given a string representing a person's name, return a greeting in the
    form of a string in the format "Hello <name> how are you today?"
    >>> greeting("Steve")
    'Hello Steve how are you today?'
    >>> greeting("123")
    'Hello 123 how are you today?'
    '''
    return "Hello " + name + " how are you today?"


def mutate_list(input_list):
    '''
    (list of int, bool, str) -> None
    REQ: input_list must have at least one element
    REQ: string elements in input_list must have at least 2 characters
    Given a list containing integers, booleans, and strings perform the
    following: multiply all integers elements  by 2, invert all booleans
    elements (true becomes false and vice versa), remove the first and last
    letters of all string elements, and set the first element to the string
    Hello, regardless of what it was originally.
    >>> input_list = ["Hello", 1, True, "five", "123", False, 76, 3.1, [1, 2]]
    >>> mutate_list(input_list)
    >>> input_list == ['Hello', 2, False, 'iv', '2', True, 152, 3.1, [1, 2]]
    True
    >>> input_list = [1]
    >>> mutate_list(input_list)
    >>> input_list == ['Hello']
    True
    >>> input_list = ["xx", "12"]
    >>> mutate_list(input_list)
    >>> input_list == ['Hello', '']
    True
    '''
    # For loop from the element at index one and perform all actions
    for i in range(1, len(input_list)):
        # Multiply integers by 2
        if type(input_list[i]) == int:
            input_list[i] = input_list[i]*2
        # Take the invert of booleans
        elif type(input_list[i]) == bool:
            input_list[i] = not input_list[i]
        # Remove the first and last letters of strings
        elif type(input_list[i]) == str:
            input_list[i] = input_list[i][1:-1]
    # Replace the first element with "Hello"
    input_list[0] = "Hello"


def merge_dicts(first_dict, second_dict):
    '''
    (dict of {str: list of ints}, dict of {str: list of ints}) ->
    dict of {str: list of ints}
    Given two dictionaries, return a new dictionary with the key:value pairs
    added to the first. If a key already exists in the first dictionary, the
    list indicated by that key in the second dictionary is appended to that of
    the first. The new dictionary is returned.
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2) == \
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    True
    >>> d1 == {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    True
    >>> merge_dicts(d2, d1) == \
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    True
    '''
    # Form a copy of the first dictionary to be returned
    ret_dict = first_dict.copy()
    # Elemental for loop through the second dictionary, check if a key
    # exist in the first dictionary. If it does not, update the return
    # dictionary with the key:value pair. If it does, append the value
    # to the existing list in the return dictionary.
    for key in second_dict:
        if key in first_dict:
            ret_dict[key] = ret_dict[key] + second_dict[key]
        else:
            ret_dict[key] = second_dict[key]
    return ret_dict
