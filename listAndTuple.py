# list  mutale the values in the list are mutale it means the values can change in the list
# Tuple  immutale the values in the tuple are immutale it means the values canNot be Changed  in the list

l1 = [5, 4, 3, 2, 1]
l2 = [-4, -3, -2]
l1.append(8)
l1[0] = 4
print(l1.__add__(l2))
# tuple
t1 = (5, 4, 3, 2, 1)
# t1[0] = -2
print(type(t1))
a = 4
b = 1
# swapp
a, b = b, a
print(a, "  ", b)

