#!/usr/bin/python3
from re import A


a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))