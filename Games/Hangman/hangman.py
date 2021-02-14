import numpy as np
import random
# Create a function that takes a number of tries. Tries must be a posive int. It should take a letter from the user within the number of tries given. If successful, return the letter or null if not a letter
def ValidateLetter(tries):
    if isinstance(tries, int) and tries > 0:
        current = 0
        while current < tries:
            if current + 1 == tries:
                letter = input("This is your last try. Please enter your choice of a letter: ")
                if letter.isalpha() and len(letter) == 1:
                    break
                else:
                    current += 1
                    letter = None
            else:
                letter = input("Please enter your choice of a letter: ")
                if letter.isalpha() and len(letter) == 1:
                    break
                else:
                    current += 1
                    letter = None
    return letter



# Maxlife = How many wrong guesses / maxtries = How many times incorrect letter input is allowed

def playhangman(word, maxlife, maxtries, HANGMANPICS):
    hangman = list(word)
    hm = np.array(hangman)
    letters = []
    length = len(word)
    result = ["_" for i in range(length)]
    result = np.array(result)
    death = 0
    tries = 0
    while death <= maxlife:
        tries += 1
        if np.array_equal(result, hm):
            print("You won! You guessed the word \"{0}\" in {1} tries and {2} wrong guesses.".format(word, tries, death))
            print(result)
            break
        elif death == maxlife:
            print("You made wrong gueses {0} times. The word was {1}. You lost!".format(death, word))
            print(HANGMANPICS[death])
            print(result)
            break
        else:
            print(HANGMANPICS[death])
            print(result)
            print("Your guesses so far: {}".format(letters))
            letter = ValidateLetter(maxtries)
            if letters.count(letter) == 0:
                indices = np.where(hm == letter)[0]
                letters.append(letter)
                #print("appended")
                if indices.size > 0:
                    for i in indices:
                        result[i] = letter
                else:
                    death += 1
                    print("Wrong guess. You just lost a life. Your life is at {} now.".format(death))
            else:
                death += 1
                print("You have entered a letter you used earlier. Please enter something different. Your life is at {} now.".format(death))


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = []
with open("hangman.txt", 'r') as f:
        for line in f:
            line = line.rstrip()
            words.append(line)
f.close()

word = random.choice(words)
playhangman(word, 6, 3, HANGMANPICS)
