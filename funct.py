# a = 7
# b = 5
# print(sum((a, b))) builtin func

def func(lst):
    """ doct string is basically used for reading the documentation of paticular module
     like ex- the function only used for taking a average of a numbers.

     """
    tot = 0
    for i in lst:
        tot = tot + i
    avg = tot / len(lst)
    return avg


lt = [5, 4, 3, 2, 1]
print(func.__doc__)
print(func(lt))
