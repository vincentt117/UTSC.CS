def edit_distance(s1, s2):
    '''(str, str) -> int
    Return the minimum number of single character changes that would be needed
    to turn s1 into s2
    '''
    # Base case
    if not s1 and not s2:
        return 0
    else:
        if s1[0] == s2[0]:
            return edit_distance(s1[1:], s2[1:])
        else:
            return 1 + edit_distance(s1[1:], s2[1:])


def subsequence(s1, s2):
    '''(str, str) -> int
    Return a boolean representing whether or not s1 is a sbusequence of s2
    '''
    # Base Cases
    # Empty s1 can always be achieved regardless of what s2 is
    if not s1:
        return True
    # If s1 is bigger, it is impossible change s2 into s1 by removing letters
    elif len(s1) > len(s2):
        return False
    else:
        if s1[0] != s2[0]:
            return subsequence(s1, s2[1:])
        else:
            return subsequence(s1[1:], s2[1:])


def perms(s):
    '''(str, str) -> set
    Return a set of all possible permutations of the letters in s
    '''
    # Base cases
    if len(s) <= 1:
        return set(s)
    elif len(s) == 2:
        return set([s, s[1] + s[0]])
    else:
        ret_set = set()
        for char in s:
            for x in perms(s.replace(char, '', 1)):
                ret_set.update(set([char + x]))
        return ret_set
