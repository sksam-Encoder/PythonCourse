num = int(input("enter a num to check armstrong"))
org = num
tot = 0


while num != 0:
    rem = num % 10
    tot = tot + (rem ** 3)
    num = int(num / 10)
if org == tot:
    print(tot)
else:
    print(tot)

