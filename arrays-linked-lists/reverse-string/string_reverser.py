""" This program takes a string as input and then returns
the reversed string.
For example, if the input is the string `water`, then the
output should be `retaw`.
"""

def string_reverser(our_string):

    """
    Reverse the input string

    Args:
        our_string(string): String to be reversed
    Returns:
        string: The reversed string
    """
    string_position = len(our_string) - 1
    reversed_string = ''

    while string_position >= 0:
        reversed_string += our_string[string_position]
        string_position -= 1

    return reversed_string


# Test Cases
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
