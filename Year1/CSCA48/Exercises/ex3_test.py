from container import *
def banana_verify(source_word, goal_word, Container, list_of_moves):
    '''
    (str, str, Container, list of str) -> bool
    REQ: Container must be implemented to function as one of: bucket, stack,
    or queue.
    REQ: list_of_moves contains only the legal moves
    Given a source word, a goal word, a container object of one of three types,
    and a list of moves represented by letters. Determine whether the given
    list of moves will allow for the source word to become the goal word
    '''
    # A string which will represent the word being built through the list of
    # moves
    temp_word = ''
    # While loop through the list of moves and perform them as
    # defined. In the event where an error occurs the move list would be
    # deemed a failure and the function will return false. At the same time
    # , track which character of the word is being viewed currently and operate
    # based on this tracking
    char_track = 0
    # Track which move that is currently being looked at
    move_num = 0
    # Tracks whether or not the moves made so far are proper
    proper = True
    while move_num < len(list_of_moves) and proper:
        if list_of_moves[move_num] == 'P':
            try:
                Container.put(source_word[char_track])
                char_track += 1
            except ContainerFullException:
                proper = False
        elif list_of_moves[move_num] == 'M':
            temp_word = temp_word + source_word[char_track]
            char_track += 1
        elif list_of_moves[move_num] == 'G':
            try :
                temp_word = temp_word + Container.get()
            except ContainerEmptyException:
                proper = False
        move_num += 1
        
    # Return whether or not the list of moves performed on the source word will
    # yield the goal word
    return temp_word == goal_word

stack = ContainerStack()
bucket = ContainerBucket()
queue = ContainerQueue()
print(banana_verify('BANANA', 'AAABN', stack, ['P', 'M', 'P', 'M', 'P', 'M', 'G', 'G', 'G']))
print(banana_verify('BANANA', 'BNAAAN', bucket, ['M', 'P', 'P', 'G', 'M', 'P', 'M', 'G']))
print(banana_verify('BANANA', 'AAANNB', stack, ['P', 'M', 'P', 'M', 'P', 'M', 'G', 'G', 'G']))
print(banana_verify('BANANA', 'BNAAAN', stack, ['M', 'P', 'M', 'G', 'M', 'P', 'M', 'G']))
print(banana_verify('BANANA', 'BNAAAN', bucket, ['M', 'P', 'M', 'G', 'M', 'P', 'M', 'G']))
print(banana_verify('BANANA', 'BNAAAN', queue, ['M', 'P', 'M', 'G', 'M', 'P', 'M', 'G']))
print(banana_verify('BANANA', 'NBNAAA', queue, ['P', 'P', 'M', 'G', 'P', 'M', 'G', 'G', 'M']))
print(banana_verify('BANANA', 'ANANAB', queue, ['P', 'M', 'M', 'M', 'M', 'M', 'G']))
print(banana_verify('BANANA', 'ANANAB', stack, ['P', 'M', 'M', 'M', 'M', 'M', 'G']))
print(banana_verify('BANANA', 'ANANAB', bucket, ['P', 'M', 'M', 'M', 'M', 'M', 'G']))
print(banana_verify('BANANA', 'NABANA', queue, ['P', 'P', 'M', 'M', 'G', 'P', 'G', 'G', 'M']))
print(banana_verify('BANANA', 'NABANA', stack, ['P', 'P', 'M', 'G', 'G', 'M', 'M', 'M']))
print(banana_verify('BANANA', 'NABANA', stack, ['P', 'P', 'P', 'P', 'P', 'M']))