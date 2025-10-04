# adventure_game.py
print("Welcome to the Dungeon Adventure!")
choice1 = input("You see two doors: left or right? ").lower()

if choice1 == "left":
    choice2 = input("You find a monster! Fight or run? ").lower()
    if choice2 == "fight":
        print("You defeated the monster! You win!")
    else:
        print("You ran away safely. Game over!")
else:
    choice2 = input("You find a treasure chest. Open or leave it? ").lower()
    if choice2 == "open":
        print("You found gold! You win!")
    else:
        print("You walked away. Game over!")
