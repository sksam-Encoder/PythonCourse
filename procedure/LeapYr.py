yr = int(input("enter  a yr"))
if yr % 4 == 0:
    print("leap yr")
elif yr % 100 == 0:
    print("leap yr")
elif yr % 400 == 0:
    print("leap yr")
else:
    print("not leap yr")
