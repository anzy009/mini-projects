import tkinter as tk
import random

words = ['python', 'django', 'hangman', 'developer', 'javascript', 'portfolio']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = random.choice(words)
        self.guessed = ['_' for _ in self.word]
        self.attempts = 6
        self.max_attempts = 6
        self.used_letters = []

        # GUI layout
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.label_word = tk.Label(root, text=' '.join(self.guessed), font=('Courier', 24))
        self.label_word.pack(pady=20)

        self.label_info = tk.Label(root, text=f"Attempts left: {self.attempts}", font=('Arial', 14))
        self.label_info.pack()

        self.label_used = tk.Label(root, text="Used letters: ", font=('Arial', 12))
        self.label_used.pack(pady=10)

        self.entry = tk.Entry(root, font=('Arial', 16), width=5, justify='center')
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.guess_letter)
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="", font=('Arial', 16))
        self.result.pack()

        self.draw_gallows()

    def draw_gallows(self):
        self.canvas.create_line(50, 250, 250, 250)  # base
        self.canvas.create_line(100, 250, 100, 50)  # pole
        self.canvas.create_line(100, 50, 180, 50)   # top beam
        self.canvas.create_line(180, 50, 180, 80)   # rope

    def draw_hangman(self):
        parts = self.max_attempts - self.attempts
        if parts >= 1:  # Head
            self.canvas.create_oval(160, 80, 200, 120)
        if parts >= 2:  # Body
            self.canvas.create_line(180, 120, 180, 180)
        if parts >= 3:  # Left Arm
            self.canvas.create_line(180, 140, 150, 120)
        if parts >= 4:  # Right Arm
            self.canvas.create_line(180, 140, 210, 120)
        if parts >= 5:  # Left Leg
            self.canvas.create_line(180, 180, 150, 220)
        if parts >= 6:  # Right Leg
            self.canvas.create_line(180, 180, 210, 220)

    def guess_letter(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not letter or len(letter) != 1 or not letter.isalpha() or letter in self.used_letters:
            return

        self.used_letters.append(letter)

        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.guessed[i] = letter
        else:
            self.attempts -= 1
            self.draw_hangman()

        self.update_display()

        if '_' not in self.guessed:
            self.result.config(text="🎉 You Win!", fg="green")
            self.button.config(state="disabled")
        elif self.attempts == 0:
            self.result.config(text=f"💀 Game Over! Word was: {self.word}", fg="red")
            self.button.config(state="disabled")

    def update_display(self):
        self.label_word.config(text=' '.join(self.guessed))
        self.label_info.config(text=f"Attempts left: {self.attempts}")
        self.label_used.config(text=f"Used letters: {', '.join(self.used_letters)}")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
