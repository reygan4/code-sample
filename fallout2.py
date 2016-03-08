import sys
import random

def count_matches(word1, word2):
    """
    Takes two strings of equal length and returns a count
    of the characters in the same position in each string.
    """
    assert len(word1) == len(word2)
    matches = 0
    for i, letter in enumerate(word1):
        if word2[i] == letter:
            matches += 1
    return matches

def get_words(length):
    """
    Opens a dictionary file and returns a list
    of all words of desired length.
    """
    words = []
    with open("enable1.txt", 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == length:
                words.append(word)
    return words

def get_guess(guesses, clues):
    """
    Asks user to guess from a selection of clues.
    Asks until their guess is one of the clues.
    Returns user's guess.
    """
    guess = input("guess ({} left) >> ".format(guesses)).lower()
    if not guess in clues:
        print("That is not one of the possibilities.")
        return get_guess(guesses, clues)
    return guess

def get_difficulty():
    """
    Asks user for the difficulty they would like to play at.
    Returns a tuple of the password length and number of clues
    appropriate for the chosen difficulty.
    """
    try:
        difficulty = int(input("select difficulty (1-5) >> "))
        assert difficulty >= 1 and difficulty <= 5
    except:
        print("Please enter a number between 1-5.")
        return get_difficulty()

    difficulty_dict = {1: (4, 5), 2: (6, 8), 3: (10, 10), 4: (12, 13), 5: (15, 15)}
    return difficulty_dict[difficulty]

def play_game():
    # set-up
    password_length, num_clues = get_difficulty()
    words = get_words(password_length)
    password = random.choice(words)
    clues = [password]
    while len(clues) < num_clues:
        clue = random.choice(words).lower()
        if not clue in clues:
            clues.append(clue)
    random.shuffle(clues)
    guesses = 4

    # play
    print("\n".join(clues))
    while guesses > 0:
        guess = get_guess(guesses, clues)
        if guess == password:
            print("you win")
            return
        matches = count_matches(password, guess)
        print("{}/{} correct".format(matches, password_length))
        guesses -= 1
    print("you lose")
    return

def main():
    play = True
    while play:
        play_game()
        play = 'y' in input("play again? (y/n) >> ").lower()

if __name__ == "__main__":
    sys.exit(main())
