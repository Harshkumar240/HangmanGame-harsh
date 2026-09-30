import random

# List of predefined words
words = ["python", "computer", "program", "developer", "coding"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum number of wrong guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)

# Create hidden version of the word
display_word = ["_"] * len(word)

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")