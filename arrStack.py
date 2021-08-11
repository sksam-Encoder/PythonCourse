

def menu():
    print("1) push a no")
    print("2) pop a no")
    print("3) capacity")
    print("4) exit")

    option = int(input("enter your choice"))

    switcher1 = {

        1: push,
        2: pop,
        3: capacity,
        4: backk

    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher1[option]()


def capacity():
    global top
    print("capacity =", top)


def backk():
    return -1


def push():
    global top
    top = top + 1
    a = (input("enter num to push"))
    stk.append(a)


def pop():
    global top
    if top == -1:
        print("stack is empty")
    else:
        item = stk.pop()
        top = top - 1
        print("pop value is", item)


stk = list()
top = -1
print(type(stk))
print(capacity())
# print(iter(int, 1))
for _ in iter(int, 5):

    b = menu()
    if b == -1:
        break

# var = iter(int, 1)
# print(next(var))
# print(next(var))
# lst = [5, 4, 3, 2, 1]
# lst = iter(lst)  # lst became an iterator object which only can be iterated of all its content
# print(next(lst))
