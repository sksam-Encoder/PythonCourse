# when a function calls itshelf then that process is called recursion
# def fun1(a):
#     print( "this is",{a})
#     fun1(a)
# fun1("sam")

# factorial
#  n! = n* (n-1)!
def factorialIter(n):
    """":param n Integer:
    :return : n*n-1 * n-2 * n-3.......n-1 = 0
    """
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
        # print("i=",i)
    return fact


#  factorial using recursions
def factorial(n):
    if n == 1:
        return  1
    else:
        return n * factorial(n-1)

# 



numbers = int(input("Enter a number"))
# print("factorial_iterative =",factorialIter(numbers))
print("factorial using recursive=",{factorial(numbers)})