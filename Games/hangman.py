# Objective - Guess a word or a phrase by guessing a letter
# User lose if a stickman is drawn
# Each incorrect guess results in a new part on a stickman - head / body / arms / legs
# User will have 6 chances for incorrect guesses. At 6th incorrect guess, the user will lose

# print("Let's play")
# input("What is your letter?")

orginalword = 'hello'
word = list(orginalword)

total_chances = 6
chance = 1
# Ask a lettera

# Assign that letter and see if it is in the wor
#
# We need to check if the user input is a letter or not.
num_letters = len(word)
print(num_letters)
underscores = "_ " * num_letters
print(underscores)

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

while (chance <= total_chances) and (len(word) != 0):
    letter = input("What is your letter? {0}".format(underscores))
    print("You entered: " + letter)
    print("You have {0} chances left.".format(chance))
    if letter in letters:
        if letter in word:
            print("Your letter {0} is in the word!".format(letter))
            word.remove(letter)
            # update underscores
            if len(word) == 0:
                print("You won! The word was '{0}'.".format(orginalword))
        else:
            chance += 1
            print(
                "Wrong guess, sucker! You just lost a chance. You are on chance #{0} now.".format(chance))

    else:
        print("Invalid")


# if letter is word:
#     print("Correct")
# else:
#     print("Incorrect")
