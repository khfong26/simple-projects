import random

word_bank = ["hello", "world", "computer", "house", "pilot"]

word_from = input("Type 1 to get a computer-generated word, type 2 to input a custom word: ")

while word_from not in ["1", "2"]:
    word_from = input("Please type 1 or 2. Type 1 for a computer-generated word, type 2 to input a custom word: ")

if word_from == "1":
    word = random.choice(word_bank)
else:
    word = input("Enter your word: ").lower()

temp_word = ["_"] * len(word)  # Represent the word with underscores
guesses = []  # List of all guessed letters
max_wrong_guesses = 6  # Max wrong guesses allowed
wrong_guesses = 0  # Current number of wrong guesses
incorrect_guesses = []  # Store wrong letters

print("\nThe word to guess:")
print(" ".join(temp_word))  # Show the word as underscores with spaces

# Main game loop
while True:
    guess = input("Please enter a letter: ").lower()

    # Input validation
    while not guess.isalpha() or len(guess) != 1 or guess in guesses:
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
        elif guess in guesses:
            print("You already guessed that letter.")
        guess = input("Please enter a letter: ").lower()

    guesses.append(guess)  # Add guess to list of guessed letters

    # Check if the guess is correct
    if guess in word:
        print(f"Good guess! The letter '{guess}' is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                temp_word[i] = guess
    else:
        wrong_guesses += 1
        incorrect_guesses.append(guess)
        print(f"Sorry, the letter '{guess}' is not in the word.")

    # Show the current state of the word and wrong guesses
    print("\nCurrent word: " + " ".join(temp_word))
    print("Wrong guesses: " + ", ".join(incorrect_guesses))
    print(f"Remaining attempts: {max_wrong_guesses - wrong_guesses}")
    print("---------------------------------------")

    # Check win or lose conditions
    if "_" not in temp_word:
        print("Congratulations! You guessed the word!")
        break
    elif wrong_guesses == max_wrong_guesses:
        print(f"Sorry, you ran out of guesses. The word was '{word}'.")
        break
