# lamda function ,or Anonymous function

# var = lambda x, y: x - y
# print(var(4, 3))

def a_first(lst):
    return lst[0]


a = [[14, 1], [4, 5], [23, 8]]
a.sort(key=lambda x: x[1])
print(a)



# print(a_first(a))
