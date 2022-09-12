#!usr/bin/python3
#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Brennan D Baraban <375@holbertonschool.com>


def safe_print_list_integers(my_list=[], x=0):
    """print the first x element of a list that are integer
    Args:
    my_list (list): the list to print element from x (int):
    the number of elemtn of my_list to print
    Returns:
    the number of elemtn print 
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
        print("")
        return (ret)
