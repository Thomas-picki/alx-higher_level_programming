#!/usr/bin/python3
def safe_print_integer(value):
    """print an intger with "{:d}".format().
    Args:
    value (int): the integer to print.
    return:\if a tupeError or valueEroor occurs - False 
    otherwise -True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
