import random


def welcome():
    kit = ["Rock", "Paper", "Scissor"]

    man_score = 0
    comp_score = 0
    win_score = 5
    results = ["Draw", "Winner", "Loser"]
    res = 0

    game = True

    print("WELCOME TO THE BEST OF THE BEST GAME ")
    print(
        '''
█████████████████████████████████████████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███████▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀██
██─▄─▄█─██─█─███▀██─▄▀██░░█████─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄██
█▄▄█▄▄█▄▄▄▄█▄▄▄▄▄█▄▄█▄▄██▄████▄▄▄███▄▄█▄▄█▄▄▄███▄▄▄▄▄█▄▄█▄▄██
█████████████████████████████████████████████████████████████
██▀▄─██▄─▀█▄─▄█▄─▄▄▀██─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█
██─▀─███─█▄▀─███─██─██▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█
█▄▄█▄▄█▄▄▄██▄▄█▄▄▄▄███▄▄▄▄▄█▄▄▄▄▄█▄▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄█▄▄█▄▄█
                                           written in python3
                                              coded by hitesh
        '''
    )

    while(game):
        print("-"*50)
        print(f"Your Score: {man_score} \t\t\t Computer Score: {comp_score}")

        comp = random.randint(0, 2)

        choice12()

        man = int(input(": "))

        print(f"Your Weapon: {kit[man-1]}")
        print(f"Computer Weapon: {kit[comp]}")
        print("\n")

        comp = comp + 1

        comp_score, man_score = AIplayer(comp_score, man_score, man, comp)

        if comp_score == win_score:
            print("Winner is Comp")
            print("You lose!")

            print("\nWant to play again")
            print("[y/n]:", end=" ")

            inp = str(input())

            if inp == 'n' or inp == 'N':
                game = False
            if inp == 'y' or inp == 'Y':
                man_score = 0
                comp_score = 0

        elif man_score == win_score:
            print("You Are Winner!")
            print("Hurray")

            print("\nWant to play again")
            print("[y/n]:", end=" ")

            inp = str(input())

            if inp == 'n' or inp == 'N':
                game = False
            if inp == 'y' or inp == 'Y':
                man_score = 0
                comp_score = 0


def choice12():
    print("\n")
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("\n")


def AIplayer(comp_score, man_score, man, comp):
    if comp == 1:   # Rock

        if man == 1:    # Rock
            print("Draw\n")
            res = 0

        elif man == 2:  # Paper
            print("You win!")
            print("Computer lose\n")
            man_score += 1
            res = 1

        elif man == 3:  # Scissor
            print("Computer wins!")
            print("You lose!\n")
            comp_score += 1
            res = 2

    elif comp == 2:  # Paper

        if man == 2:  # Paper
            print("Draw\n")
            res = 0

        elif man == 3:  # Scissor
            print("You win!")
            print("Computer lose\n")
            man_score += 1
            res = 1

        elif man == 1:  # Rock
            print("Computer wins!")
            print("You lose!\n")
            comp_score += 1
            res = 2

    elif comp == 3:  # Scissor

        if man == 3:    # Scissor
            print("Draw\n")
            res = 0

        elif man == 1:  # Rock
            print("You win!")
            print("Computer lose\n")
            man_score += 1
            res = 1

        elif man == 2:  # Paper
            print("Computer wins!")
            print("You lose!\n")
            comp_score += 1
            res = 2
    return comp_score, man_score


welcome()
