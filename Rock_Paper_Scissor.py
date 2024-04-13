import random
while True:
    user_action = input("Enter a choice (Stone, Paper, Scissors):")
    possible_actions = ["Stone", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou Choose {user_action}, Computer Choose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Stone":
        if computer_action == "Scissors":
            print("Stone smashes Scissors! You win!")
        else:
            print("Paper covers Stone! You lose.")
    elif user_action == "Paper":
        if computer_action == "Stone":
            print("Paper covers Stone! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Stone smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break