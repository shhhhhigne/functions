"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.



###############################################################################

# I wasnt sure if this was supposed to take a hometown as a argument as well or
# if it's a set hometown 
def is_hometown(town):
    """Takes a town name as a string and returns True if it is berkeley
    
    >>> is_hometown('berkeley')
    True

    >>> is_hometown('rodeo')
    False
    """

    if town.lower() == 'berkeley':
        return True

    return False


def concat_first_last_name(first, last):
    """Take a first name and a last name and concatenates them to return as one 
    string
    
    >>> concat_first_last_name('Signe', 'Henderson')
    'Signe Henderson'
    """

    return first + " " + last


# Im not sure why this isnt returning the right thing, the outputs look identical
# to me
def string_concat(hometown, first, last):
    """Take a first name, last name and hometown and using other functions 
    have a small conversation about them

    >>> string_concat('berkeley', 'Signe', 'Henderson')
        Hi Signe Henderson, where are you from?
        Hi Signe Henderson,, we're from the same place!
    """

    name = concat_first_last_name(first, last)
    print "    Hi " +  name + ", where are you from?"

    if is_hometown(hometown):
        print "    Hi " + name + ", we're from the same place!"
 


# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit in ['strawberry', 'cherry', 'blackberry']:
        return True
    
    return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit):
        return 0

    return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    lst[:] = lst + [num]

    return lst



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.


# Im not sure how you guys formatted your numbers and I cant figure out how to do 
# it so I get the exact same outputs as you, but the numbers all look right
def calculate_price(base_price, state, tax = .05):
    """Take the base price of something and caluclate the cost with tax and add
    any potential state specific fees
    """

    price = (base_price * tax) + base_price

    if state == "CA":
        price = (price * .03) + price

    elif state == 'PA':
        price = price + 2.00

    elif state == 'MA':
        if base_price <  100:
            price = price + 1.00
        else:
            price = price + 3.00
     

    price = "{0:3f}".format(price)
    return float(price)


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

def add_to_list(lst, *args):
    """This function takes a list and an unspecified number of arguments and 
    returns that list with the arguments appended to the end 

    >>> add_to_list(['a', 'b', 'c', 'd'], 'e', 'f', 'g', 'h')
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    """

    for item in args:
        lst[:] = lst + [item]

    return lst

def nester(word):
    """This function takes a word and using an inner function returns that word
    along with that same word *3

    >>> nester('dog')
    ('dog', 'dogdogdog')

    """

    def nested():
        return word *3
    words = nested()
    
    return word, words


# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
