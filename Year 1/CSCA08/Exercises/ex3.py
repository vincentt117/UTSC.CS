def percent_to_gpv(percent_mark):
    '''
    Takes in the percent mark in integer form and returns the corresponding
    Grade Point Value (float).
    (int) --> float
    REQ: percent_mark >= 0
    REQ: percent_mark <= 100
    >>> percent_to_gpv(100)
    4.0
    >>> percent_to_gpv(85)
    4.0
    >>> percent_to_gpv(84)
    3.7
    >>> percent_to_gpv(80)
    3.7
    >>> percent_to_gpv(79)
    3.3
    >>> percent_to_gpv(77)
    3.3
    >>> percent_to_gpv(76)
    3.0
    >>> percent_to_gpv(73)
    3.0
    >>> percent_to_gpv(72)
    2.7
    >>> percent_to_gpv(70)
    2.7
    >>> percent_to_gpv(69)
    2.3
    >>> percent_to_gpv(67)
    2.3
    >>> percent_to_gpv(66)
    2.0
    >>> percent_to_gpv(63)
    2.0
    >>> percent_to_gpv(62)
    1.7
    >>> percent_to_gpv(60)
    1.7
    >>> percent_to_gpv(59)
    1.3
    >>> percent_to_gpv(57)
    1.3
    >>> percent_to_gpv(56)
    1.0
    >>> percent_to_gpv(53)
    1.0
    >>> percent_to_gpv(52)
    0.7
    >>> percent_to_gpv(50)
    0.7
    >>> percent_to_gpv(49)
    0.0
    >>> percent_to_gpv(0)
    0.0
    '''
    # Based on the given mark, determine which range it belongs to and return
    # the corresponding gpv.
    if (percent_mark >= 85):
        return 4.0
    elif(84 >= percent_mark >= 80):
        return 3.7
    elif(79 >= percent_mark >= 77):
        return 3.3
    elif(76 >= percent_mark >= 73):
        return 3.0
    elif(72 >= percent_mark >= 70):
        return 2.7
    elif(69 >= percent_mark >= 67):
        return 2.3
    elif(66 >= percent_mark >= 63):
        return 2.0
    elif(62 >= percent_mark >= 60):
        return 1.7
    elif(59 >= percent_mark >= 57):
        return 1.3
    elif(56 >= percent_mark >= 53):
        return 1.0
    elif(52 >= percent_mark >= 50):
        return 0.7
    else:
        return 0.0


def card_namer(value, suit):
    '''
    Takes two single character strings, representing the value and suit
    of a card following the shorthand below, and returns the full name of the
    card.
    (str, str) --> str
    REQ: suit == Diamonds or suit == Clubs, suit == Hearts, suit == Spades
    >>> card_namer('Q','D')
    'Queen of Diamonds'
    >>> card_namer('9','S')
    '9 of Spades'
    >>> card_namer('8','T')
    'CHEATER!'
    '''
    cardname = ""
    # Based on given value, determine corresponding English word to include
    # in the first portion of the string
    if(value == "A"):
        cardname = "Ace of "
    elif(value == "T"):
        cardname = "10 of "
    elif (value == "J"):
        cardname = "Jack of "
    elif (value == "Q"):
        cardname = "Queen of "
    elif (value == "K"):
        cardname = "King of "
    else:
        cardname = value + " of "
    # Based on suit, determine the corresponding English word to incorparate
    # in the second portion of the string. In the event where the suit is not
    # one of the four suits, return "CHEATER!" instead
    if(suit == "D"):
        cardname += "Diamonds"
    elif(suit == "C"):
        cardname += "Clubs"
    elif(suit == "H"):
        cardname += "Hearts"
    elif(suit == "S"):
        cardname += "Spades"
    else:
        cardname = "CHEATER!"
    return cardname


def my_str(param):
    '''
    Takes an object as input and returns a string representation of that object
    (obj) - > str
    >>> my_str("Hello")
    'Hello'
    >>> my_str(True)
    'YES'
    >>> my_str(False)
    'NO'
    >>> my_str(10)
    'Small Number'
    >>> my_str(11)
    'Medium Number'
    >>> my_str(99)
    'Medium Number'
    >>> my_str(100)
    'Large Number'
    >>> my_str(42.0)
    '42.0'
    >>> my_str(3.1415926)
    '3.14'
    >>> my_str([1, 2, 3])
    'I dunno'
    '''
    # Evaluates cases where the input is a string
    if(type(param) == str):
        return param
    # Evaluates cases where the input is a boolean
    elif(type(param) == bool):
        if(param is True):
            return "YES"
        else:
            return "NO"
    # Evaluates cases where the input is an interger
    elif(type(param) == int):
        if(param <= 10):
            return "Small Number"
        elif(param > 10 and param <= 99):
            return "Medium Number"
        else:
            return "Large Number"
    # Evaluates cases where the input is a float
    elif(type(param) == float):
        return str(round(param, 2))
    # Evaluates cases where the input is not one of the four data types
    else:
        return "I dunno"
