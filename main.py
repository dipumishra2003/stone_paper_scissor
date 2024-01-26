import random

user_score = 0
comp_score = 0

print("Welcome to stone, paper and scissor game! ")
response = input("Are you want to play game? ")

if response.lower() != "yes":
    quit()

option = ["stone", "paper", "scissor"]

while True:
    action = input("Enter stone/paper/scissor or q to quit :").lower()

    if action == "q":
        break

    elif action not in option:
        continue

    number = random.randint(0, 2)
    # stone=0, paper=1, scissor=2

    print("Computer picked : ", option[number])

    if action.lower() == "stone" and number == 0:
        print("correct!")
        user_score += 1

    elif action.lower() == "paper" and number == 1:
        print("correct!")
        user_score += 1

    elif action.lower() == "scissor" and number == 2:
        print("correct!")
        user_score += 1

    else:
        print("Incorrect!")
        comp_score += 1


total = str(user_score + comp_score)
user_score = str(user_score)
comp_score = str(comp_score)
print("Your score is " + user_score + " out of " + total)