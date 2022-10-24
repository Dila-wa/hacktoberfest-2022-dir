import random

you = input("Select Rock, Paper, or Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Player 2 selected: ", player2)

if you == "rock" and player2 == "paper":
    print("Player 2 Won")
elif you == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif you == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif you == player2:
    print("Tie")
else:
    print("You Won The Game")
