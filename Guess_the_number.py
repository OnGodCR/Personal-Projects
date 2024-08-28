import random

tries = 0
print("Let's play guess the number!")
number = random.randrange(1,100)
x = int(input("I am thinking of a number between 1 and 100, guess the number! "))
while x!=number:
    if x>100 or 1>x:
        x=input("The number you entered was invalid, please try again. The range is 1-100 ")
    elif x>number:
        x = int(input("That number was too big! Try guessing a smaller number! "))
        tries= tries+1
    elif x<number:
        x= int(input("That number was too small! Try guessing a bigger number! "))
        tries=tries+1
if x == number:
    print("You guessed it! The number was indeed ", x)
    print("You took", tries, "tries!")