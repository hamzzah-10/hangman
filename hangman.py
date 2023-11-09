import random 
from words import words
import string

# print(words)

def get_valid_words(words):
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_words(words)  
    #print(word)      
    word_letters = set(word)
    #print(word_letters)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word ", ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                print("\nYour letter is not in word.")
        elif user_letter in used_letters:
            print(f"\nThis letter {user_letter} is already guessed. Please guess another letter.")
        else:
            print("\nNot a valid character.")    


    print(f"You have guessed the word {word}.")




hangman()    

