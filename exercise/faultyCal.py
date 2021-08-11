# faulty calculator
a = int(input("enter 1st number"))
b = int(input("enter 2st number"))
sym = input("enter the operator? +, - , /, % ,* ")

if a == 45 and b == 3 and sym == '*':
    print("555")
elif a == 56 and b == 9 and sym == '+':
    print('77')
elif a == 56 and b == 6 and sym == '/':
    print('4')
elif sym == '+':
    total = a + b
    print('sum =', total)
elif sym == '-':
    total = a - b
    print("subtraction =", total)
elif sym == '*':
    total = a * b
    print("Multiplication =", total)
elif sym == '/':
    total = a / b
    print("divide =", total)
