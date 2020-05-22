#!/usr/bin/python3
"""text indentation class"""


def text_indentation(text):
    """ splits and adds lines"""

    s = ""
    if isinstance(text, str) is False or None:
        raise TypeError("text must be a string")
    for i in (text):
        s += i
        if i in ":?.":
            print(s.lstrip(), end="\n\n")
            s = ""
    print(s.lstrip(), end="")
