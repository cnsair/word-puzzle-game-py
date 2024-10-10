'''
AUTHOR: Chisom Samson Nwachukwu

PURPOSE: W04 Prove: Word Puzzle

Shows Creativity and Exceeds Requirements: 
    Line 19: I used the random.choice() function to select a word from a list
    Line 18 & 54: I introduced a while loop to enable the user play again
    Line 27 - 36: I used a function to give the hints to a player
'''
import random

print()
print('Welcome to the Word Puzzle Game')


play_again = 'yes'

#for i, secret in enumerate(secret_word):
while play_again == 'yes':
    
    secret_word = random.choice(['ensign', 'brigham', 'worldwide', 'puzzle', 'pathway']) # randomly selects a new word for each loop
    secret_word_len = len(secret_word) # Gets the length of the secret work

    guess_count = 0 # Reset guess_count for the new game
    guess_word = '' # Reset the guess_word for a new loop

    def get_hint(secret_word, guess):
        hint = []
        for i in range(len(guess)):
            if guess[i] == secret_word[i]:
                hint.append(guess[i].upper())  # Correct letter and position
            elif guess[i] in secret_word:
                hint.append(guess[i].lower())  # Correct letter but wrong position
            else:
                hint.append('_')  # Incorrect letter
        return ''.join(hint)

    while secret_word != guess_word:
        guess_word = input('Make your guess: ').lower()
        guess_word_len = len(guess_word)

        guess_count = guess_count + 1

        if secret_word_len != guess_word_len:
            print(f'Word\'s length does not match. Secret word is {secret_word_len} letters')
        elif secret_word == guess_word:
            print('Correct! You guessed right!')
        else:
            hint = get_hint(secret_word, guess_word)
            print(f"Hint: {hint}")

    print(f'You made {guess_count} guesses')

    play_again = input('Play again (yes/no)? ').lower()

print('Goodbye! We\'ll miss you')