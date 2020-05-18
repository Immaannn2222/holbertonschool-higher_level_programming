#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as frr:
        print("Exception: {}".format(frr), file=sys.stderr)
        return None
