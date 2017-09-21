import random
num1=(1,6)
num2=(1,6)
roll_dice ="yes"
while roll_dice=="yes" or roll_dice=="y":
    print"Do you want to roll the dice?"
    print random.randint(num1,num2)