""" A bad app to practice debugging """

import random

def getinput():
    """ Get the guess from the user and return it as an int """
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return 1 if guess == 'heads' else 0

def main():
    """ The main program """
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    guess = getinput()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = getinput()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

main()

# ORIGINAL CODE:
#
# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guesss = input()
#     if toss == guess:
#        print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')
