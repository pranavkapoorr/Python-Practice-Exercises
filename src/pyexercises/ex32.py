# coding: iso-8859-1
'''
Exercise 32 (and Solution)
This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).
In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
In this exercise, we have to put it all together and add logic for handling guesses.
Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
Optional additions:
When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!
'''
import random

def pick_random_word():
    """
    This function picks a random word from the SOWPODS
    dictionary. 
    """
    # open the sowpods dictionary
    with open("resources/ex30/sowpos.txt", 'r') as f:
        words = f.readlines()

    # generate a random index
    # -1 because len(words) is not a valid index into the list `words`
    index = random.randint(0, len(words) - 1)

    # print out the word at that index
    word = words[index].strip()
    return word


def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)


if __name__ == '__main__':
    WORD = pick_random_word()

    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0

    print("Welcome to Hangman!")
    while (len(letters_to_guess) > 0) and num_guesses < 6:
        guess = ask_user_for_next_letter()

        # check if we already guessed that
        # letter
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed:
            # print out a message
            print("You already guessed that letter.")
            continue

        # if the guess was correct
        if guess in letters_to_guess:
            # update the letters_to_guess
            letters_to_guess.remove(guess)
            # update the correct letters guessed
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            # only update the number of guesses
            # if you guess incorrectly
            num_guesses += 1

        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(6 - num_guesses))

    # tell the user they have won or lost
    if num_guesses < 6:
        print("Congratulations! You correctly guessed the word {}".format(WORD))
    else:
        print("Sorry, you list! Your word was {}".format(WORD))