import random
number = random.randint (1,20)
guesses = 5

for i in range (guesses): 
    guess = int(input("what is your guess =>"))
    if(number == guess):
        print("we have a winner")
    else:
        print("we have a loser")

print("number:", number)