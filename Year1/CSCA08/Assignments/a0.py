# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Vincent Teng
# MarkUs Login: tengvinc
#


PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # your code here

    occurance = 0
    # Counts the number of occurences of the string in its intial position
    # from left to right, and adds it to the mounting sum of int occurance.
    # The puzzle is then rotated and the processes is repeated (3 times) until
    # counts from all four directions have been recorded. Return this sum

    # Count from left to right and rotate puzzle
    occurance += lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)

    # Count from top to bottom and rotate puzzle
    occurance += lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)

    # Count from right to left and rotate puzzle
    occurance += lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)

    # Count from bottom to top
    occurance += lr_occurrences(puzzle, word)
    return occurance

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> bool
    Given the puzzle and a word to search for, return a boolean if the word
    occurs from left-to-right and/or right-to-left
    >>> in_puzzle_horizontal(PUZZLE1, 'brian')
    True

    >>> in_puzzle_horizontal(PUZZLE1, 'pnnz')
    True

    >>> in_puzzle_horizontal(PUZZLE1, 'paco')
    False
    '''
    counter = 0
    # A counter will record the number of occurrences of the word from
    # left-to-right then right-to-left in the given puzzle. If the counter
    # records a quantity greater than zero (hence the word exists in the puzzle
    # horizontally) the function returns true, else it returns false

    # Counts from left to right and rotates puzzle twice
    counter += lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)
    puzzle = rotate_puzzle(puzzle)

    # Counts from right to left
    counter += lr_occurrences(puzzle, word)
    return counter >= 1


# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> bool
    Given the puzzle and a word to search for, return a boolean representing if
    the word occurs from top-to-bottom and/or bottom-to-top

    >>> in_puzzle_vertical(PUZZLE1, 'paco')
    True

    >>> in_puzzle_vertical(PUZZLE1, 'pnnz')
    False
    '''
    counter = 0
    # A counter will record the number of occurrences of the word from
    # top-to-bottom then bottom-to-top in the given puzzle. If the counter
    # records a quantity greater than zero (hence the word exists in the puzzle
    # vertically) the function returns true, else it returns falsee
    puzzle = rotate_puzzle(puzzle)

    # Count from top-to-bottom
    counter += lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)
    puzzle = rotate_puzzle(puzzle)

    # Count from bottom-to-top
    counter += lr_occurrences(puzzle, word)
    return counter >= 1

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str, str) -> bool
    Given the puzzle and a word to search for, return a boolean representing if
    the word occurs atleast once, in any direction

    >>> in_puzzle(PUZZLE1, 'brian')
    True

    >>> in_puzzle(PUZZLE1, 'python')
    False
    '''
    # Calling the function total_occurrences will provide the number of times
    # the given word occurs in the puzzle, thus a returned value of 1 or
    # greater suggests that the word does exist in the puzzle. Return a
    # boolean representing whether or not this is true
    return total_occurrences(puzzle, word) >= 1

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''(str, str) -> bool
    Given the puzzle and a word to search for, return a boolean representing if
    the word occurs in only one dimension

    >>> in_exactly_one_dimension(PUZZLE1, 'brian')
    False

    >>> in_exactly_one_dimension(PUZZLE1, 'paco')
    True

    >>> in_exactly_one_dimension(PUZZLE1, 'python')
    False
    '''
    # If the word occurs in only one dimension, only one of either
    # in_puzzle_horizontal or in_puzzle_vertical will return true. Logically
    # if the two statements are inequivalent (one is true the other is false)
    # the word occurs in only one direction, else in both cases (true or false
    # for both functions) the word exists in either both dimensions or neither,
    # respectively
    return in_puzzle_horizontal(puzzle, word) is not \
        in_puzzle_vertical(puzzle, word)


# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str, str) -> bool
    Given the puzzle and a word to search for, return a boolean representing
    if the word occurs exclusively in the horizontal directions or not at all
    in the puzzle

    >>> all_horizontal(PUZZLE1, 'brian')
    False

    >>> all_horizontal(PUZZLE1, 'pnnz')
    True

    >>> all_horizontal(PUZZLE1, 'python')
    True
    '''
    # Based on the description of the function, as long as the word does not
    # occur vertically, the function will return True. Logically, it is
    # the opposite of in_puzzle_vertical, thus we return the opposite of
    # in_puzzle_vertical's return value
    return not in_puzzle_vertical(puzzle, word)


# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str, str) -> bool
    Given the puzzle and a word to search for, return a boolean representing
    if the word occurs once and once vertically

    >>> at_most_one_vertical(PUZZLE1, 'brian')
    False

    >>> at_most_one_vertical(PUZZLE1, 'pnnz')
    False

    >>> at_most_one_vertical(PUZZLE1, 'paco')
    True
    '''

    # The word must not occur at all horizontally and most occur only once
    # vertically in order for the return to be True, all other scenarios will
    # return False. Thus we return the opposite of in_puzzle_horizontal's
    # return value and whether or not total_occurrences returned exaclty 1
    return not in_puzzle_horizontal(puzzle, word) and \
        total_occurrences(puzzle, word) == 1


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print(lr_occurrences(puzzle, name))

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    puzzle = rotate_puzzle(puzzle)
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences(puzzle, name))

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    puzzle = rotate_puzzle(puzzle)
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(puzzle, name))

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    puzzle = rotate_puzzle(puzzle)
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(puzzle, name))

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print(total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, 'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE2, 'anya'))
