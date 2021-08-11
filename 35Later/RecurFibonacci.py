# 0  1  1  2   3   5    8


def fibo_Recur(n):
    if n <= 1:
        return n
    else:
        return fibo_Recur(n - 1) + fibo_Recur(n - 2)




def fiboIter(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        tot = a + b
        a = b
        b = tot

# fiboIter(6)
for i in range(5):
    print(fibo_Recur(i))


