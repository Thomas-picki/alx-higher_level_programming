#!/usr/bin/python3
def to_uper(ch):
    if ord(ch) >= 97 and ord(ch) <= 122:
        return (ord(ch) - 32)
    else:
        return ord(ch)

    def uppercase(string):
        string_new = ""
        for ch in string:
            string_new += "%c" % to_uper(ch)
            print("{:s}".format(string_new))
