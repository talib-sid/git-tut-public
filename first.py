import random

def checkNum(num):
    if num > 50:
        print("Greater than 50")
    else:
        print("Less than 50")


myNum = random.randint(1, 100)
checkNum(myNum)


def Checkifnegative(num):
    if num < 0:
        print("Negative")
    else:
        print("Positive")
