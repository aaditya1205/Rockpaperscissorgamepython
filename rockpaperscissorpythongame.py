import random

# Choices and their mappings
computer = random.choice([0, 1, 2])  # 0: Rock, 1: Paper, 2: Scissors
youDict = {"r": 0, "p": 1, "s": 2}
reversedict = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Get user input
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
if youstr not in youDict:
    print("Invalid choice. Please choose 'r', 'p', or 's'.")
    exit()

you = youDict[youstr]

# Display choices
print(f"You chose {reversedict[you]} \nComputer chose {reversedict[computer]}")

# Determine the result
if computer == you:
    print("It's a draw!")
elif (computer == 0 and you == 1) or (computer == 1 and you == 2) or (computer == 2 and you == 0):
    print("You win!")
else:
    print("You lose!")
