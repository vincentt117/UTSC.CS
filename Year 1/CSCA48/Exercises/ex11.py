from container import *


def banana_game(s1, s2, c):
    '''(str, str, container ADT) -> bool
    Returns whether c can turn s1 into s2 via the rules of the banana game
    >>> banana_game('BANANA', 'BANANA', ContainerQueue())
    True
    >>> banana_game('BANANA', 'BANANA', ContainerBucket())
    True
    >>> banana_game('BANANA', 'BANANA', ContainerStack())
    True

    >>> banana_game('BANANA', 'AAANNB', ContainerQueue())
    False
    >>> banana_game('BANANA', 'AAANNB', ContainerBucket())
    False
    >>> banana_game('BANANA', 'AAANNB', ContainerStack())
    True

    >>> banana_game('BANANA', 'BNAAAN', ContainerQueue())
    True
    >>> banana_game('BANANA', 'BNAAAN', ContainerBucket())
    True
    >>> banana_game('BANANA', 'BNAAAN', ContainerStack())
    True

    >>> banana_game('BANANA', 'NBNAAA', ContainerQueue())
    True
    >>> banana_game('BANANA', 'NBNAAA', ContainerBucket())
    False
    >>> banana_game('BANANA', 'NBNAAA', ContainerStack())
    False

    >>> banana_game('BANANA', 'NNAAAB', ContainerQueue())
    False
    >>> banana_game('BANANA', 'NNAAAB', ContainerBucket())
    False
    >>> banana_game('BANANA', 'NNAAAB', ContainerStack())
    True

    >>> banana_game('BANANA', 'ANANAB', ContainerQueue())
    True
    >>> banana_game('BANANA', 'ANANAB', ContainerBucket())
    True
    >>> banana_game('BANANA', 'ANANAB', ContainerStack())
    True

    >>> banana_game('BANANA', 'NABANA', ContainerQueue())
    True
    >>> banana_game('BANANA', 'NABANA', ContainerBucket())
    False
    >>> banana_game('BANANA', 'NABANA', ContainerStack())
    True
    '''
    if not s2:
        return not s1 and c.is_empty()
    else:
        if s1 and s1[0] == s2[0]:
            # Length one strings that are equal
            if len(s1) == 1 and len(s2) == 1:
                return c.is_empty()
            # s1 is length 1
            elif len(s1) == 1 and len(s2) != 1 and\
                    banana_game('', s2[1:], c.copy()):
                return True
            elif len(s1) != 1 and len(s2) != 1 and\
                    banana_game(s1[1:], s2[1:], c.copy()):
                return True
            elif len(s1) != 1 and len(s2) == 1:
                return False
        # Attempt to check if the first element retrieved from the container is
        # the first element of s2
        try:
            if c.peek() == s2[0]:
                c.get()
                if len(s2) == 1:
                    return not s1 and c.is_empty()
                else:
                    return banana_game(s1, s2[1:], c)
        except (ContainerEmptyException):
            pass
        # Attmept to place the first letter of s1 into c
        try:
            if s1:
                c.put(s1[0])
                if len(s1) == 1:
                    return banana_game('', s2, c)
                else:
                    return banana_game(s1[1:], s2, c)
        except (ContainerFullException):
            pass
    return False
