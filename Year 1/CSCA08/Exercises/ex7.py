def create_dict(file_handle):
    ''' (io.TextIOWrapper) -> dict of [str: [str, str, str, int, str]}
    Given an opened text file, return a dictionary where the key is the
    "user name" in each line and the value each key points to is a
    list containing the last name, first name, e-mail, age, and gender of the
    line, in that order.
    REQ: Text lines in opened text file must be in the specified format
    >>> file_handle = open('ex7_data.txt', 'r')
    >>> create_dict(file_handle) == {'ajones': \
    ['Jones', 'Alice', 'alice@alicejones.ne', 44, 'F'], \
    'rford': ['Ford', 'Rob', 'robford@crackshack.com', 44, 'M'], \
    'cmangler': ['Mangler', 'Code', 'cm@mangler.net', 103, 'F'], \
    'bharrington': ['Harrington', 'Brian', 'brian.harrington@utsc.utoronto.ca'\
    , 33, 'M'], \
    'ncheng': ['Cheng', 'Nick', 'nick@utsc.utoronto.ca', 17, 'M'], \
    'asmith': ['Smith', 'Alice', 'alice.smith@utsc.utoronto.ca', 31, 'F']}
    True

    '''
    ret_dict = {}
    # Loop through the lines in the text file
    for next_line in file_handle:
        # Temporary list which will hold the strings in the current line of the
        # file
        tl = []
        # Loop through the separated strings in the textfile and place each
        # string separated by a white space as an element in the temporary
        # list.
        last_space = 0
        for i in range(len(next_line)):
            if (next_line[i] == ' ' or i == len(next_line) - 1):
                tl.append(next_line[last_space:i].strip())
                last_space = i
        # With the formatting of each line in the textfile being identical,
        # each element would only need to be placed in the dictionary value
        # list by a predetermined index
        ret_dict[tl[0]] = [tl[2], tl[1], tl[5], int(tl[3]), tl[4]]
    return(ret_dict)


def update_field(my_dict, user_name, field, new_val):
    ''' (dict of {str: [str, str, str, int, str]}, str, str, str or int) ->
    NoneType
    Given a dictionary of the format of function create_dict's return,
    a username, the name of a field(One of: ’LAST’, ’FIRST’, ’E-MAIL’, ’AGE’ or
    ’GENDER’), and a new value to replace the current value of the specified
    field. Return None and mutate the dictionary as appropriate
    REQ: my_dict formatted as specified
    REQ: if new_val is an int, it must be 0 or greater
    REQ: field is one of: ’LAST’, ’FIRST’, ’E-MAIL’, ’AGE’ or
    ’GENDER’
    >>> my_dict = {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 999, 'M']}
    True
    >>> my_dict = {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'GENDER', 'F')
    >>> my_dict == {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'F']}
    True
    >>> my_dict = {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'FIRST', 'Steve')
    >>> my_dict == {'sclause':\
    ['Clause', 'Steve', 'santa@christmas.np', 450, 'M']}
    True
    >>> my_dict = {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'LAST', 'Jack')
    >>> my_dict == {'sclause':\
    ['Jack', 'Santa', 'santa@christmas.np', 450, 'M']}
    True
    >>> my_dict = {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'E-MAIL', 'sc@gmail.com')
    >>> my_dict == {'sclause':\
    ['Clause', 'Santa', 'sc@gmail.com', 450, 'M']}
    True
    '''
    # Dictionary with key as all-caps field (that which is given as parameter)
    # pointing towards index in value (of my_dict) list that correspond to the
    # field. Thus, change the element at the index corresponding to the field
    # to the new value
    ref_dict = {'LAST': 0, 'FIRST': 1, 'E-MAIL': 2, 'AGE': 3, 'GENDER': 4}
    my_dict[user_name][ref_dict[field]] = new_val
    return None


def select(my_dict, sel_field, che_field, val):
    '''(dict of {str: [str, str, str, int, str]}, str, str, str or int) ->
    set()
    Given a dictionary of the format of function create_dict's return, the
    name of a field to select, the name of a field to check, and a value to
    check for, return a set of all the data elements from the selected fields
    of key whose checked fields were equal to the checked value
    REQ: my_dict formatted as specified
    REQ: If val is an int, it must be greater than or equal to zero
    REQ: sel_field and che_field are one of: ’LAST’, ’FIRST’, ’E-MAIL’, ’AGE’
    or ’GENDER’
    >>> my_dict = {'sclause':\
    ['Clause', 'Santa', 'santa@christmas.np', 450, 'M'],\
    'ebunny':['Bunny', 'Easter', 'bunny@easter.hop', 99, 'M'],\
    'tfairy':['Fairy', 'Tooth', 'fairy@money4teeth.net', 0, 'F']}
    >>> select(my_dict, 'E-MAIL', 'GENDER', 'M')
    {'santa@christmas.np', 'bunny@easter.hop'}
    '''
    ret_set = set()
    # Dictionary with key as all-caps field (that which is given as parameter)
    # pointing towards index in value (of my_dict) list that correspond to the
    # field
    ref_dict = {'LAST': 0, 'FIRST': 1, 'E-MAIL': 2, 'AGE': 3, 'GENDER': 4}
    # Loop through the dictionary by key and add the select value of keys
    # which possess the desired check field value
    for akey in my_dict.keys():
        if(my_dict[akey][ref_dict[che_field]] == val):
            ret_set.add(my_dict[akey][ref_dict[sel_field]])
    return ret_set
