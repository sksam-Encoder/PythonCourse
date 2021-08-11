# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, which must be unique
# the other 3 are List, Tuple, and Dictionary,
# all with different qualities and usage.
#

# Unordered
# Unordered means that the items in a set do not have a defined order.
#   it like an tuple also
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.


s1 = {5, 4, 3, 2, 1, 2}
s2 = {6, 7, 8, 9, 0, 1, 3, 4}
print(type(s1))
print(s1.union(s2))
print(s2.intersection(s1))
s3 = {2,1,3}
s4 = {4,5,6}
print(s3.isdisjoint(s4))
s1.add(10)
# s1.pop()
print(s1)