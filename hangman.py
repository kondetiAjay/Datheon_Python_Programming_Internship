
import random

# ASCII gallows stages
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def load_words():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words = [
                line.strip().upper()
                for line in file
                if line.strip().isalpha()
            ]

        if words:
            return words

    except FileNotFoundError:
        pass

    # Fallback words
    return ["PYTHON", "COMPUTER", "PROGRAMMING", "SCIENCE"]


def play_game():
    secret_word = random.choice(load_words())
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\nWelcome to Hangman!")
    print("Guess the secret word one letter at a time.")

    while wrong_guesses < max_attempts:
        # Display current game status
        masked_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", masked_word)
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print("Attempts remaining:", max_attempts - wrong_guesses)

        # Check victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The word was:", secret_word)
            return

        guess = input("Enter one letter: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).\n")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        guessed_letters.add(guess)

        # Correct or incorrect guess
        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    # Display final result
    print(HANGMAN_PICS[wrong_guesses])
    print("You lost! Better luck next time.")
    print("The secret word was:", secret_word)


if __name__ == "__main__":
    play_game()
