# import random
# toss = random.randint(0,1)
# if toss == 1:
#     print("head")
# else:
#     print("tail")
#
# import random
# while True:
#     names = input("Enter names ")
#     l1 = names.split()
#     i = len(l1)
#     c = random.randint(0 , i-1)
#     pay = l1[c]
#     print(f" {pay} is going to pay bill")
#
#     play_again = input("play again (Y/N) ").lower()
#     if play_again == 'n':
#         break
#

# rock paper scissors

import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
