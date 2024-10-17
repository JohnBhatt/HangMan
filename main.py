#Step 5
import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


#Testing code
print(hangman_art.logo)
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Your Guess is not in the list of words. One Life is reduced. Remaining chance(s) : {lives}")
        if lives == 0:
            end_of_game = True
            print("Sorry, you exhausted all the lives. You lose.")
    if guess in chosen_word:
      print("You have already guessed the word, correctly.")


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])