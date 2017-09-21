import random
num1=(1)
num2=(6)
roll_dice ="yes"
while roll_dice=="yes" or roll_dice=="y":
    print "You rolled..."
    print random.randint(num1,num2)
    print random.randint(num1,num2)
    roll_dice=raw_input("Would you like to roll the dice again?")
     