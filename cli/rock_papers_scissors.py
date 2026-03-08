import random

# rock paper scissors
# made by las-r on github

# game vars
choices = ["rock", "paper", "scissors"]
winner = ""

while not winner:
    # choice
    botchoice = random.choice(choices)
    userchoice = input("Enter your move: ").lower()
    while userchoice not in choices:
        print("Invalid.")
        userchoice = input("Enter your move: ")
        
    # check winner
    if botchoice == "rock":
        if userchoice == "paper": winner = "user"
        elif userchoice == "scissors": winner = "bot"
        else: print("Draw, go again.")
    elif botchoice == "paper":
        if userchoice == "scissors": winner = "user"
        elif userchoice == "rock": winner = "bot"
        else: print("Draw, go again.")
    else:
        if userchoice == "rock": winner = "user"
        elif userchoice == "paper": winner = "bot"
        else: print("Draw, go again.")

# results
if winner == "user": print(f"You won! I chose `{botchoice}` and you chose `{userchoice}`.")
else: print(f"I won! I chose `{botchoice}` and you chose `{userchoice}`.")
