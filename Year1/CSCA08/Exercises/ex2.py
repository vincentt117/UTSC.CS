# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5
a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50

def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    '''
    return raw_mark / max_mark * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    >>> raw_contribution(13.5, 15, 10)
    9.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    '''
    return (raw_mark/max_mark*weight)
    
def term_work_mark(a0_mark, a1_mark, a2_mark, exercises_mark, quizzes_mark, term_tests_mark):
    ''' (int, int, int, int, int, int) --> (float)
    Given the mark recieved on the six elements of the course, return the term mark out of a maximum of 55
    >>> term_work_mark(0,0,0,0,0,0)
    0.0
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    55.0
    >>> term_work_mark(20, 45, 70, 8, 4, 40)
    43.9
    REQ: 0 <= a0_mark <= 25
    REQ: 0 <= a1_mark <= 50
    REQ: 0 <= a2_mark <= 100
    REQ: 0 <= exercises_mark <= 10
    REQ: 0 <= quizzes_mark <= 5
    REQ: 0 <= term_tests_mark <= 50
    '''
    return (contribution(a0_mark, a0_max_mark, a0_weight) + contribution(a1_mark,a1_max_mark,a1_weight) + contribution(a2_mark,a2_max_mark,a2_weight) + contribution(exercises_mark,exercises_max_mark,exercises_weight) + contribution(quizzes_mark,quizzes_max_mark,quizzes_weight) + contribution(term_tests_mark,term_tests_max_mark,term_tests_weight))

def final_mark(a0_mark, a1_mark, a2_mark, exercises_mark, quizzes_mark, term_tests_mark, exam_mark):
    ''' (int, int, int, int, int, int, int) --> (float)
    Given the mark recieved on the seven elements of the course, return the final mark out of a maximum of 100
    >>> final_marl(0,0,0,0,0,0,0)
    0.0
    >>> final_mark(25, 50, 100, 10, 5, 50,100)
    100.0
    >>> final_mark(20, 45, 70, 8, 4, 40, 73)
    76.75
    REQ: 0 <= a0_mark <= 25
    REQ: 0 <= a1_mark <= 50
    REQ: 0 <= a2_mark <= 100
    REQ: 0 <= exercises_mark <= 10
    REQ: 0 <= quizzes_mark <= 5
    REQ: 0 <= term_tests_mark <= 50
    REQ: 0 <= exam_mark <= 100
    '''    
    return term_work_mark(a0_mark, a1_mark, a2_mark, exercises_mark, quizzes_mark, term_tests_mark) + contribution(exam_mark, exam_max_mark, exam_weight)

def is_pass(a0_mark, a1_mark, a2_mark, exercises_mark, quizzes_mark, term_tests_mark, exam_mark):
    ''' (int, int, int, int, int, int, int) --> (boolean)
    Given the mark recieved on the seven elements of the course, return a boolean (a combination of whether term mark exceeds passing threshold, and whether exam mark exceeds passing threshold) representing whether the indvidual has passed
    >>> is_pass(0,0,0,0,0,0,100)
    False
    >>> is_pass(25,50,100,10,5,50,0)
    False
    >>> is_pass(20, 45, 70, 8, 4, 40, 41)
    True
    >>> is_pass(20, 45, 70, 8, 4, 40, 39)
    False
    >>> is_pass(10, 21, 12, 2, 1, 15, 23)
    False
    REQ: 0 <= a0_mark <= 25
    REQ: 0 <= a1_mark <= 50
    REQ: 0 <= a2_mark <= 100
    REQ: 0 <= exercises_mark <= 10
    REQ: 0 <= quizzes_mark <= 5
    REQ: 0 <= term_tests_mark <= 50
    REQ: 0 <= exam_mark <= 100    
    '''
    return (final_mark(a0_mark, a1_mark, a2_mark, exercises_mark, quizzes_mark, term_tests_mark, exam_mark) >= overall_pass_mark and exam_mark >= exam_pass_mark)
       
           
                  
    
    
