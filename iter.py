lst = [5, 4, 3, 2, 1]
lst = iter(lst)
# lst became a list operator which can't be print but can be iterate through next()
print(next(lst))
var = iter(int, 1)
print(next(var))
