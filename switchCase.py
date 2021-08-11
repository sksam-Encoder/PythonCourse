# Function to convert number into string
# Switcher is dictionary data type here
def one():
    return "one"


def two():
    return "two"


def three():
    return "three"


def numbers_to_strings(argument1):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: -1
    }
    # calling function using brackets

    return switcher[argument1]()


# Driver program

for _ in iter(int, 1):
    print("enter a argument in 1) 2) 3) 4) to exit")
    argument = int(input("enter chose"))
    print(str(numbers_to_strings(argument)))
