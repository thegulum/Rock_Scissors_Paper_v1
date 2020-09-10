from random import randint

t = ["Rock", "Scissors", "Paper"]

computer = t[randint(0, 2)]

player = False

while not player:
    player = input("Rock, Paper, Scissors ? : ")
    if player == computer:
        print("It's a tie!")
    elif player.capitalize() == "Rock":
        if computer == "Paper":
            print("---You lose!", computer, "covers", player)
        else:
            print("---You win!", player, "smashes", computer)
    elif player.capitalize() == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("---You win!", player, "covers", computer)
    elif player.capitalize() == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    elif player == "quit":
        exit()
    else:
        print("You have a typo, please, check again!")

    player = False
    computer = t[randint(0, 2)]
