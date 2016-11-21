"""

# 2013, 2014, 2015, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2016
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.


def is_regex(s):
    '''(str) -> bool
    Return whether the string s is a valid regular expression
    >>> is_regex('0')
    True
    >>> is_regex('00')
    False
    >>> is_regex('1')
    True
    >>> is_regex('2')
    True
    >>> is_regex('e')
    True
    >>> is_regex('0*')
    True
    >>> is_regex('**')
    False
    >>> is_regex('1*')
    True
    >>> is_regex('2*')
    True
    >>> is_regex('e*')
    True
    >>> is_regex('(0|1)')
    True
    >>> is_regex('()')
    False
    >>> is_regex('(0*|2*)')
    True
    >>> is_regex('((0.1).2)')
    True
    >>> is_regex('((1.(0|2)*).0)')
    True
    >>> is_regex('(((1.(0|2))*).0)')
    False
    >>> is_regex('abc')
    False
    >>> is_regex('()|()')
    False
    '''
    # Length 1 regex
    if s in '012e' and len(s) == 1:
        return True
    # '*' regex
    elif len(s) >= 2 and s[-1] == '*':
        return is_regex(s[:-1])
    # '.' or '|' regex
    elif len(s) >= 5 and s[0] == '(' and s[-1] == ')':
        # Find the '' or '|' associated with the outer brackets and determine
        # if the substring on the left and right hand side of that entity
        # are valid regexs

        # Traverse by index. Upon finding '.' or '|' split the string at that
        # point and call the function with the two parts as parameters,
        # excluding the most outer brackets. If '(' is found, continue until
        # all '(' on the left side are found and an equal number of ')' are
        # found; the '.' or '|' afterwards is the associated operation.

        lr_bracket_balance = 0
        count = 1
        while count < len(s) - 1:
            if (s[count] == '.' or s[count] == '|') and\
               lr_bracket_balance == 0:
                return is_regex(s[1:count]) and is_regex(s[count + 1: -1])
            elif s[count] == '(':
                lr_bracket_balance += 1
            elif s[count] == ')':
                lr_bracket_balance -= 1
            count += 1
    # In the event where none of these conditions are true, the string is not
    # a valid regex.
    return False


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
{'(2|0**)', '(0|2**)', '(2|0*)*', '(2*|0)*', '(0**|2)', '(0|2*)*',\
'(2|0)**', '(2*|0*)', '(0|2)**', '(0*|2)*', '(0*|2*)', '(2**|0)'}
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
    # Singular ternary string case
    if s in '012e':
        return set([s])
    # Ternary string with trailing stars case
    elif s.replace('*', '') in '012e':
        # Find the ternary string and move it to the front
        for i in '012e':
            if i in s:
                return set([i + s.replace(i, '')])
    # Cases with '|', '.'
    else:
        if (s.count('0') + s.count('1') + s.count('2') + s.count('e')) - 1\
           == s.count('.') + s.count('|') and \
           2*(s.count('.') + s.count('|')) == s.count('(') + s.count(')'):
            # Check for non regex characters
            s_dup = s
            for i in '012e.()|*':
                s_dup = s_dup.replace(i, '')
            if not s_dup:
                # Form all permutations strings
                temp = all_regex_permutations_helper(s)
                ret = set()
                for i in temp:
                    if is_regex(i):
                        ret.add(i)
                return ret
    return set()


def all_regex_permutations_helper(s):
    '''(str) -> set of str
    Return a set of all valid regex permutations of string s
    '''
    if len(s) <= 1:
        return set(s)
    elif len(s) == 2:
        return set([s, s[1] + s[0]])
    else:
        ret_set = set()
        for char in s:
            for x in all_regex_permutations_helper(s.replace(char, '', 1)):
                # Permutations where certain elements are adjacent will b
                # omitted
                sym_or_op = ''
                valid = True
                count = 0
                temp = char + x
                while valid and count < len(temp) - 1:
                    if temp[count] in '012e':
                        if temp[count + 1] in '(012e':
                            valid = False
                    elif temp[count] in '.|':
                        if temp[count + 1] in '*.|':
                            valid = False
                    count += 1
                if valid:
                    ret_set.update(set([char + x]))
        return ret_set


def regex_match(r, s):
    '''(RegexTree, s) -> bool
    Returns whether the regex s matches the regex tree rooted at r
    >>> regex_match(build_regex_tree('0'), '0')
    True
    >>> regex_match(build_regex_tree('e'), '')
    True
    >>> regex_match(build_regex_tree('e'), 'e')
    False
    >>> regex_match(build_regex_tree('2*'), '2')
    True
    >>> regex_match(build_regex_tree('(0|1)'), '0')
    True
    >>> regex_match(build_regex_tree('(0.1)'), '01')
    True
    >>> regex_match(build_regex_tree('((1.(0|2)*).0)'), '122220')
    True
    '''
    # r is Leaf
    if type(r) is Leaf:
        # s must be an empty string if the symbol of r is 'e'
        if r.get_symbol() == 'e':
            return not s
        # Otherwise, s must be exactly the string stored in r
        else:
            return r.get_symbol() == s
    # r is BarTree
    elif type(r) is BarTree:
        # Split s at all possible indices and call this function via r's left
        # right child on the split parts of s. If at one iteration, one of
        # the two function call returns true, s matches r.
        ind = 0
        match = False
        while ind <= len(s) and not match:
            match = regex_match(r.get_left_child(), s[:ind]) or\
                regex_match(r.get_right_child(), s[ind:])
            ind += 1
        return match
    # r is DotTree
    elif type(r) is DotTree:
        # Split s at all possible indices and call this function via r's left
        # right child on the split parts of s. If at one iteration, both of
        # the two function call returns true, s matches r.
        ind = 0
        match = False
        while ind <= len(s) and not match:
            match = regex_match(r.get_left_child(), s[:ind]) and\
                regex_match(r.get_right_child(), s[ind:])
            ind += 1
        return match
    # r is StarTree
    else:
        # If s is empty, it will match the tree
        if not s:
            return True
        # In the event where s is non-empty
        # Split s at all possible indices and call this function on the left
        # portion of the split. If the portion matches r's child and removing
        # all substrings of s identitical to the split results in an empty
        # string, then s matches r.
        ind = 0
        match = False
        while ind <= len(s) and not match:
            if regex_match(r.get_child(), s[:ind]):
                match = not s.replace(s[:ind], '')
            ind += 1
        return match


def build_regex_tree(regex):
    '''(str) -> RegexTree
    Builds the RegexTree as specified by the valid regex parameter. Return
    this tree's root
    REQ: regex is a valid regex
    '''
    # Length 1 regex
    if len(regex) == 1:
        return Leaf(regex)
    # '*' regex
    elif regex[-1] == '*':
        return StarTree(build_regex_tree(regex[:-1]))
    # '.' or '|' regex
    else:
        # Find the '' or '|' associated with the outer brackets and build
        # two children rooted to the '.' or '|' tree

        # Traverse by index. Upon finding '.' or '|' split the string at that
        # point and call the init with the two parts as parameters,
        # excluding the most outer brackets. If '(' is found, continue until
        # all '(' on the left side are found and an equal number of ')' are
        # found; the '.' or '|' afterwards is the associated operation.

        lr_bracket_balance = 0
        count = 1
        while count < len(regex) - 1:
            if regex[count] == '.' and lr_bracket_balance == 0:
                return DotTree(build_regex_tree(regex[1:count]),
                               build_regex_tree(regex[count + 1: -1]))
            elif regex[count] == '|' and lr_bracket_balance == 0:
                return BarTree(build_regex_tree(regex[1:count]),
                               build_regex_tree(regex[count + 1: -1]))
            elif regex[count] == '(':
                lr_bracket_balance += 1
            elif regex[count] == ')':
                lr_bracket_balance -= 1
            count += 1
