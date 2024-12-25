import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number.")

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlyaer", player_idx + 1, "turn has started!")
        print("Your score is: ", player_scores[player_idx], "\n")


        current_score = 0

        while True:  

            should_roll = input("Would you like to roll? (y/n): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1. Your turn is skipped.")
                current_score = 0
                break
            else: 
                current_score += value
                print("You rolled a", value)
                print("Your current score is", current_score)

        player_scores[player_idx] += current_score
        print(f"Your total score is {player_scores[player_idx]}")

winner = max(player_scores)
winning_idx = player_scores.index(winner)
print("\nGame over!")
print("The winner is Player", winning_idx + 1, "with a score of", winner)