#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp = tuple_a + (0, 0)
    trd = tuple_b + (0, 0)
    return ((tmp[0] + trd[0]), (tmp[1] + trd[1]))
