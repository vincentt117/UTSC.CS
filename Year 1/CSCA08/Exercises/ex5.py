def function_names(filename):
    '''(io.TextIOWrapper) -> list os str

    Takes a file open for reading and returns a list of all the
    function names in the file
    >>> filename = open('ex4.py', 'r')
    >>> function_names(filename)
    ['insert', 'up_to_first', 'cut_list']
    '''

    # Detects lines containing function decloration and append the function
    # name into a list. Once the entire script has been scanned, return
    # the list
    return_list = []
    for next_line in filename:
        if(next_line.startswith('def ')):
            return_list.append(next_line[4:next_line.index('(')])

    return(return_list)


def justified(filename):
    '''(io.TextWrapper) -> bool

    Takes a file open for reading and returns a boolean representing whether
    or not all text lines in teh file are left-justified
    >>> filename = open('ex5_just_all_left.txt', 'r')
    >>> justified(filename)
    True

    >>> filename = open('ex5_just_not_left.txt', 'r')
    >>> justified(filename)
    False
    '''
    # Scenarios in which the line begins with spaces and is not an empty line
    # will cause the entire file to be deemed as not left justified
    for next_line in filename:
        if(next_line.startswith(" ") and not len(next_line) == 0):
            return False
    return True


def section_average(filename, sec_code):
    '''(io.TextWrapper, string) -> float

    Given a file open for reading containing information regarding students and
    a section code, return the average midterm mark for students in that
    section
    >>> filename = open('ex5_grade_file.txt', 'r')
    >>> section_average(filename, "LEC01")
    17.25

    >>> filename = open('ex5_grade_file.txt', 'r')
    >>> section_average(filename, "LEC02")
    18.25

    >>> filename = open('ex5_grade_file.txt', 'r')
    >>> section_average(filename, "LEC30")
    12.25

    >>> filename = open('ex5_grade_file.txt', 'r')
    >>> section_average(filename, "LEC07")

    '''

    # Extract string 5 characters (the number of characters in a section code)
    # following the occurance of the section code within a line in the file.
    # Parse this into a float and added to a mounting sum. Divide this sum by
    # the number times the section code occurs to return the average mark
    mark_sum = 0.0
    mark_count = 0
    for next_line in filename:
        if(sec_code in next_line):
            mark_count += 1
            mark_sum += float(next_line[next_line.index(sec_code) + 5:])

    # Return None if the section code is not found within the file
    if(mark_count == 0):
        return None
    return(mark_sum / mark_count)
