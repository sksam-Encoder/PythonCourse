def sumOf(n):
    if n == 1:
        return 1
    else:
        return n + sumOf(n - 1)




print(sumOf(5))
