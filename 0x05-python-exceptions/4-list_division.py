#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for x in range(list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except (ZeroDivisionError):
            res = 0
            print("division by 0")
        except (TypeError):
            res = 0
            print("wrong type")
        except (IndexError):
            res = 0
            print("out of range")
        finally:
            new.append(res)
    return new
