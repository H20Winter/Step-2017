
# creates a new list called food that is empty
food = ["cheese", "milk", "butter", "bananna", "bread", "souls of the innocent", "grapes", "bagels"]

food.append("ice cream")
food.append("nut mix")

print(food)
i = 0

while i < len(food):
    print(food[i])
    i = i + 1

for i in range(len(food)):
    print(food[i])