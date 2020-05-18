#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as edr:
        print("Exception: {}".format(edr), file=sys.stderr)
        return False
