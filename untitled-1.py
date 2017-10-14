answer = random.radint(43, 1000)

guess = int(input("input a number 0 to 1000: "))

if guess < 0 and guess > 1000:
    print("that isn't on the list")
    
elif guess is answer:
    print ("yee your right")

elif guess is 42:
    print("it's the answer to most things but not this")
    
else:
    print("you're a loooser you're a loooser.")
