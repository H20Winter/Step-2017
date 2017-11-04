import random

win = "false"


while win == "false":
    ai = random.randint (1, 5)
    guess = int(input("Pick 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for spock => "))
    
    if guess == ai:
        print("tie")
    
    elif guess is 1:
        if ai == 2:
            print("rock is covers by paper. YOU FAILED")
        elif ai == 4:
            print("rock smashes lizard. Victory")
            win = "winning"
        elif ai == 5:
            print("Spock vaporizes Rock. YOU FAILED")
        else:
            print("Rock smashes scissors. Victory.")
            win = "winning"
    
    elif guess is 2:
        if ai == 3:
            print("paper is chopped by scissors. YOU FAILED")
        elif ai == 4:
            print("Paper is eaten by lizard. YOU FAILED")
        elif ai == 5:
            print("Paper is about stuff that disproves spock. Victory")
            win = "winning"
        else:
            print("Paper smothers rock. victory")
            win = "winning"
    
    elif guess is 3:
        if ai is 1:
            print("scissors is crushed by rock. YOU FAILED")
        else:
            print("scissors sliced and diced up paper. Victory")
            win = "winning"
    else:
        print("you made an hand gesture that looked like the spawn of a demon and had to go to the hospital. but the gesuture made the ai so scared it died. Congrats")