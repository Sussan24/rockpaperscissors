import random
print("Welcome to ROCK, PAPER OR SCISSORS GAME!")
print('"R" for "rock", "P" for "paper", "S" for "scissors".')
print("Lets begin!")

while True:
    choices = ['R', 'P', 'S']

    cpu = random.choice(choices)
    player = input("R, P, or S?: ").upper()

    opt = {
        'R': "Rock",
        'S': "Scissors",
        'P': "Paper"
    }
    print(f"player({opt.get(player)}) : cpu({opt.get(cpu)})")

    if player == cpu:
        print("cpu: ", cpu)
        print("player: ", player)
        print("Tie!")

    elif player == "R":
        if cpu == "P":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "S":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You win!")
        break

    elif player == "S":
        if cpu == "R":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "P":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You win!")
        break

    elif player == "P":
        if cpu == "S":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "R":
            print("cpu: ", cpu)
            print("player: ", player)
            print("You win!")
        break

    elif player != choices:
        print("incorrect choice!, try again")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
