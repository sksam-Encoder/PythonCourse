# Snake ,Water , Gun Game
import random

tme = int(input("How many times you want to play Game"))
t1 = list()
t1.append("Snake")
t1.append("Water")
t1.append("Gun")

cpu = random.choice(t1).lower()
for i in range(tme):
    usr = input("enter one of the in snake,water,gun").lower()
    if usr == "snake":
        if cpu == "water":
            print("You Wins !")
        elif cpu == "gun":
            print("Computer Wins")
        else:
            print("Game Tie")
    elif usr == "water":
        if cpu == "snake":
            print("Computer Wins")
        elif cpu == "gun":
            print("You Wins !")
        else:
            print("Game Ties")
    else:
        if cpu == "water":
            print("Computer Wins")
        elif cpu == "snake":
            print("You Wins !")
        else:
            print("Game Ties")












