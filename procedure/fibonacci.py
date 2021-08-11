n = int(input("enter numbers of terms"))
a, b = 0, 1
total = int
for i in range(0, n):
    print(a, end=" ")
    total = a + b
    a = b
    b = total
