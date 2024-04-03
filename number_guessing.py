import random
import math
#input lower number
lower= int(input("ENter the lower number: "))
#input higher number
upper= int(input("ENter the higher number: "))

#generating a random number from lower and upper range
Machine_num= random.randint(lower, upper)
print("\n\tYou will have only ", 
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the right number!\n")

#Initializing the number of total guesses.
gusses = 0


#the calculation of minimum number of
#guesses depends upon range
while gusses < math.log(upper - lower + 1, 2):
    gusses += 1

     #guessing number as input
    User_guess = int(input("Guess a number:- "))

    # Implement Condition testing
    if Machine_num == User_guess:
        print("Congratulations you did it in ",
              gusses, " try")
        # Once guessed, loop will break
        break
    elif Machine_num > User_guess:
        print("You guessed too small!")
    elif Machine_num < User_guess:
        print("You Guessed too high!")

# If user guessing is more than targeted guesses
# then shows this output.
if gusses >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % Machine_num)
    print("\tBetter Luck Next time!")
 