import random

rand_num=random.randint(0,20)
while True:
    num= int(input("Guess number between 0-20: "))
    if num!= rand_num:
        print("wrong guess, Try again!")
    elif num==rand_num:
        print("correct guess!")
        break    
    