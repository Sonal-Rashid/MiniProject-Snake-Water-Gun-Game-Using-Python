import random

def game(user, computer):
    # draw
    if user == computer:
        return None

    # Snake vs. Water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

    # Water vs. Gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

    # Gun vs. Snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


# Score counters
wins = 0
losses = 0
draws = 0

while True:
    # Computer's turn
    computer = random.choice(["s", "w", "g"])
    # Your turn
    user = input("Choose Snake(s), Water(w), Gun(g): ").lower()

    if user not in ("s", "w", "g"):
        print("Invalid choice! Enter s, w, or g.")
        continue

    print(f"You chose: {user} and Computer chose: {computer}")

    result = game(user, computer)

    if result is None:
        print("It's a draw!")
        draws += 1
    elif result:
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Current score: Wins={wins}, Losses={losses}, Draws={draws}")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print("\n--- Final Score ---")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Draws: {draws}")
print("Thanks for playing!")
