# Rock Paper Scissors
# Player vs Computer with score tracking

import random

options = ["rock", "paper", "scissors"]

# what beats what
beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif beats[player] == computer:
        return "player"
    else:
        return "computer"

def display_result(player, computer, result):
    icons = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    print(f"\n  You:      {icons[player]} {player.capitalize()}")
    print(f"  Computer: {icons[computer]} {computer.capitalize()}")

    if result == "tie":
        print("  → It's a tie!\n")
    elif result == "player":
        print("  → You win this round! 🎉\n")
    else:
        print("  → Computer wins this round.\n")

def main():
    print("=== Rock Paper Scissors ===")
    print("Type 'r' for rock, 'p' for paper, 's' for scissors, 'q' to quit\n")

    player_score = 0
    computer_score = 0
    rounds = 0

    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:
        user_input = input("Your move: ").strip().lower()

        if user_input == "q":
            break

        player_choice = shortcuts.get(user_input, user_input)

        if player_choice not in options:
            print("Invalid choice. Use r, p, s, or q.")
            continue

        computer_choice = random.choice(options)
        result = get_winner(player_choice, computer_choice)

        display_result(player_choice, computer_choice, result)

        rounds += 1
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"  Score — You: {player_score}  Computer: {computer_score}  (Round {rounds})\n")

    # final summary
    print("\n=== Game Over ===")
    print(f"Rounds played: {rounds}")
    print(f"Your score:    {player_score}")
    print(f"Computer:      {computer_score}")

    if player_score > computer_score:
        print("You win overall! 🏆")
    elif computer_score > player_score:
        print("Computer takes the match.")
    else:
        print("Overall tie!")

if __name__ == "__main__":
    main()
