# Guessing game

import random
print("You only have 5 chances to guess the number: ")
x = random.randint(1,10)
for chance in range (5):
    guess = int(input("Enter your guess (1 to 10)"))
    if (guess == x):
        print("You guessed it right!!!")
        print(guess,"==",x)
        break
    else:
        chances = 5-(chance+1)
        if chances == 0:
            print("Sorry, No more chances left")
        else:
            print("Wrong!, you have only",chances,"chances left")
