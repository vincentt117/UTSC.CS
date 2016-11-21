def all_regex_permutations(s):
    '''(str) -> set
    Return a set of all permutations of s which are valid regex
    >>> all_regex_permutations('0')
    {'0'}
    >>> all_regex_permutations('9')
    set()
    >>> all_regex_permutations('0*')
    {'0*'}
    >>> all_regex_permutations('*0')
    {'0*'}
    >>> all_regex_permutations('(0|1)') == {'(0|1)', '(1|0)'}
    True
    >>> all_regex_permutations('(0*|2*)') ==\
{'(0|2*)*', '(0*|2)*', '(0*|2*)', '(2|0*)*', '(2*|0*)', '(2*|0)*'}
    True
    >>> all_regex_permutations('((0.1).2)') == \
    {'(2.(1.0))', '((0.1).2)', '(1.(0.2))', '((2.0).1)', '((0.2).1)',\
'((1.2).0)', '(2.(0.1))', '(0.(2.1))', '((1.0).2)', '(0.(1.2))', '(1.(2.0))',\
'((2.1).0)'}
    True
    >>> all_regex_permutations('0*|(1)') == \
    {'(1|0*)', '(0|1)*', '(0*|1)', '(1*|0)', '(1|0)*', '(0|1*)'}
    True
    '''
    # Simple cases, length of one or two
    if len(s) == 1 and is_regex(s):
        return set([s])
    elif len(s) == 2:
        if is_regex(s):
            return set([s])
        elif is_regex(s[1] + s[0]):
            return set([s[1] + s[0]])
    # Cases where '.', '|' may exist
    elif len(s) >= 5:
        dup_s = s
        # Determine the quantity of each regex symol
        s_tra = {'0': 0, '1': 0, '2': 0, 'e': 0, '(': 0, ')': 0, '*': 0,
                 '.': 0, '|': 0}
        for i in '012e()*.|':
            s_tra[i] += dup_s.count(i)
            dup_s.replace(i, '')
        # Call the recursive helper to form regex permutations of s
        # if the characters of s allows for regex permutations
        if not dup_s or s_tra['('] == s_tra[')'] or s_tra['('] <\
           (s_tra['.'] + s_tra['|']) or\
           (s_tra['0'] + s_tra['1'] + s_tra['2'] + s_tra['e']) <\
           (2 * s_tra['.'] + 2 * s_tra['|']) or\
           s_tra['*'] > (s_tra['0'] + s_tra['1'] + s_tra['2'] + s_tra['e']\
                         + s_tra[')']):
            return all_regex_permutations_helper(s_tra)
    else:
        return set()

def all_regex_permutations_helper(symb_dict):
    '''
    (dict of str to ints) -> set of str
    Return a set of regex permutations given the number of each symbol
    REQ: symb_dict contains a number of symbols that can be used to make
    valid regex
    
    # Base case
    '''