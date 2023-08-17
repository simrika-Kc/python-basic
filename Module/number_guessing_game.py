import random
num=random.randint(1,100)
user=int(input("enter any number you want to guess between 1 to 100: "))
if user>num:
    print("your gussing number is high ")
elif user<num:
    print("your guessing number is low")
else:
    print("compuer guessing:= ",num)
    print("congratulation!!,Your guessing and computer guessing is same")