#!/usr/bin/python3
# 1-elemnt_at.py

def element_at(my_list, idx):
    """retrive an element fro the list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
        return (my_list[idx])