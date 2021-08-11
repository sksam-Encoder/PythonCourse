n = int(input("enter no of rows"))
b = {"si": True, "no": False}[input("enter true or false").lower()]
if b:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print("")
else:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print("")
