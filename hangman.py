# hangman.py
import random
words = ["python","django","javascript","developer","portfolio"]
word = random.choice(words)
guessed = ["_"]*len(word)
attempts = 6

while attempts>0 and "_" in guessed:
    print("Word: "," ".join(guessed))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i, c in enumerate(word):
            if c==guess:
                guessed[i]=guess
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")
if "_" not in guessed:
    print("You Win!", word)
else:
    print("Game Over! Word was:", word)
