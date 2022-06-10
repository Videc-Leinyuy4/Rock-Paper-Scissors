import random

choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
player = False
cpu_score = 0
player_score = 0

while True:
    player = input("Enter your choice: \nR - rock, P - paper, S - scissors: ").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == "R":
       player = "rock"
    elif player == "P":
       player = "paper"
    elif player== "S":
       player = "scissors"
    else:
      print("Wrong input! Enter: rock, paper or scissors!")
      print("Computer: ", computer)
    if computer == player:
      print("it's a tie!")
    elif computer== "paper" and player == "rock" or computer == "rock" and player == "scissors" or computer == "scissors" and player == "paper":
      print("Game over!")
    elif computer== "paper" and player == "scissors" or computer == "rock" and player == "paper" or computer == "scissors" and player == "rock":
      print("Congratulations! You won!!!")
      break