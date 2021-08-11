yr = int(input("enter an yr"))

if yr % 4 == 0 or (yr % 100 == 0 and yr % 400 == 0):
    print("Leap year")
else:
    print("not leap yr")
