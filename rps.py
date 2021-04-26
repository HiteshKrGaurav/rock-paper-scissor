import random

name = str(input("Enter your name: "))


def welcome():
    kit = ["Rock", "Paper", "Scissor"]

    man_score = 0
    comp_score = 0
    win_score = 5

    game = True

    print("WELCOME TO THE BEST OF THE BEST GAME ")
    print(
        '''
███████████████████████████████████████████████████████████████
██▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄████████▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀██
███─▄─▄█─██─█─███▀██─▄▀██████████─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄██
██▄▄█▄▄█▄▄▄▄█▄▄▄▄▄█▄▄█▄▄████████▄▄▄███▄▄█▄▄█▄▄▄███▄▄▄▄▄█▄▄█▄▄██
██████████████─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀███████████
██████████████▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄███████████
██████████████▄▄▄▄▄█▄▄▄▄▄█▄▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄█▄▄█▄▄███████████
                                             written in python3
                                                coded by hitesh
_______________________________________________________________
            Note: If You choose invalid value, 
                random value will be taken 
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        '''
    )

    print(f"winning score: {win_score}")

    while(game):
        print("‾"*62)
        print(
            f" {name}: {man_score}                           Bot: {comp_score}")

        comp = random.randint(0, 2)

        choice12()

        man = int(input(": "))

        if man != 1 or man != 2 or man != 3:
            print(f"{name} has enter invalid value.")
            print("Hence, a random weapon has been taken.\n")
            man = random.randint(1, 3)

        print(f"{name}r Weapon: {kit[man-1]}")
        print(f"Computer Weapon: {kit[comp]}")
        print("\n")

        comp += 1

        comp_score, man_score = AIplayer(comp_score, man_score, man, comp)

        if comp_score == win_score:
            print("Winner is Bot")
            print(f"{name} is loser!")
            print(f"{name} defeated by Bot")

            print("\nWant to play again")
            print("[y/n]:", end=" ")

            inp = str(input())

            if inp == 'n' or inp == 'N':
                game = False
            if inp == 'y' or inp == 'Y':
                man_score = 0
                comp_score = 0

        elif man_score == win_score:
            print(f"{name} Are Winner!")
            print("Hurray")
            print(f"{name} defeated a Bot!")

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

        elif man == 2:  # Paper
            print(f"{name} win!")
            man_score += 1

        elif man == 3:  # Scissor
            print(f"{name} lose!\n")
            comp_score += 1

    elif comp == 2:  # Paper

        if man == 2:  # Paper
            print("Draw\n")

        elif man == 3:  # Scissor
            print(f"{name} win!")
            man_score += 1

        elif man == 1:  # Rock
            print(f"{name} lose!\n")
            comp_score += 1

    elif comp == 3:  # Scissor

        if man == 3:    # Scissor
            print("Draw\n")

        elif man == 1:  # Rock
            print(f"{name} win!")
            man_score += 1

        elif man == 2:  # Paper
            print(f"{name} lose!\n")
            comp_score += 1
    return comp_score, man_score


welcome()
