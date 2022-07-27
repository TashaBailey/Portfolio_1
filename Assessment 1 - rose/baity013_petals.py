# File      : baity013_petals
# Author    : Tasha Bailey
# Stud Id   : 110378613
# Email Id  : baity013
# Description: Programming Assignment 1 - Petals Around the Rose
# This is my own work as defined by the University's Academic Misconduct policy.

# Start.
print('File      : baity013_petals')
print('Author    : Tasha Bailey')
print('Stud Id   : 110378613')
print('Email Id  : baity013')
print('Description: Programming Assignment 1 - Petals Around the Rose')
print('This is my own work as defined by the University\'s Academic Misconduct policy.')

print('Petals Around the Rose')
print('----------------------')
print('The name of the game is \'Petals Around the Rose\'. The name of the game is important. The computer will roll five dice and ask you to guess the score for the roll. The score will always be zero or an even number. Your mission, should you choose to accept it, is to work out how the computer calculates the score. If you succeed in working out the secret and guess correctly four times in a row, you become a Pontentate of the Rose.')

# Import dice and random.
import dice
import random

# Simulate randomly generated roll of dice.
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
die3 = random.randint(1, 6)
die4 = random.randint(1, 6)
die5 = random.randint(1, 6)

# Display dice to user.
dice.display_dice(die1, die2, die3, die4, die5)

# Prompt user for their guess
# userGuess = int(input('Please enter your guess for the roll: '))

# Formula for petal around the rose.

petal3 = 0
petal5 = 0

if die1 == 3:
    petal3 = petal3 + 2
if die2 == 3:
    petal3 = petal3 + 2
if die3 == 3:
    petal3 = petal3 + 2
if die4 == 3:
    petal3 = petal3 + 2
if die5 == 3:
    petal3 = petal3 + 2
if die1 == 5:
    petal5 = petal5 + 4
if die2 == 5:
    petal5 = petal5 + 4
if die3 == 5:
    petal5 = petal5 + 4
if die4 == 5:
    petal5 = petal5 + 4
if die5 == 5:
    petal5 = petal5 + 4

# print(petal3, petal5) # Test

# Add petals togethers to get total
totalPetals = petal3 + petal5
# print(totalPetals)

# If user guesses correctly, display message.
# If user guesses an incorrect NON EVEN number, display message.
# If user guesses an inncorrect EVEN number, display message.

# Add code to keep track of:
    # How many games were played.
    # The number of correct guesses.
    # The number of incorrect guesses.
# Display this to the screen.

wins = 0
losses = 0
gamesPlayed = 0

# Validate user input for leave

# Loop until the user enters 'n' to quit the game.
leave = input('Would you like to play Petals Around the Rose [y|n]?: ')

# If user wants to leave without playing the game.
if leave == 'n':
    print('No worries... another time perhaps... :)')

while leave != 'y' and leave != 'n':
    print('Please enter either \'y\' or \'n\'')
    leave = input('Would you like to play Petals Around the Rose [y|n]?: ')

while leave != 'n':
    # Prompt user for their guess
    userGuess = int(input('Please enter your guess for the roll: '))

    # If user guesses correctly, display message.
    # If user guesses an incorrect NON EVEN number, display message.
    # If user guesses an inncorrect EVEN number, display message.

    if userGuess == totalPetals:
        print('Well done! You guessed it!')
        wins = wins + 1
        if wins == 4:
            print('Congradulations! You have worked out the secret!')
            print('Make sure you don\'t tell anyone!')
    elif userGuess != totalPetals and userGuess % 2 != 0:
        print('No sorry, it\'s', totalPetals, 'not', userGuess, '. The score is always even.' ,sep=' ')
        losses = losses + 1
        if losses == 4:
            print('Hint: The name of the game is important... Petals around the rose.')
    else:
        print('No sorry, it\'s ', totalPetals, ' not ', userGuess, '.', sep='')
        losses = losses + 1
        if losses == 4:
            print('Hint: The name of the game is important... Petals around the rose.')

    gamesPlayed = gamesPlayed + 1
    leave = input('Would you like to play Petals Around the Rose [y|n]?: ')
    # Data validation for leave.
    while leave != 'y' and leave != 'n':
        print('Please enter either \'y\' or \'n\'')
        leave = input('Would you like to play Petals Around the Rose [y|n]?: ')

# Game summary for user.
print('Game Summary')
print('============')
print('You have played', gamesPlayed, 'games:')
print('  |--> Number of correct guesses:    ', wins)
print('  |--> Number of incorrect guesses:  ', losses)
print('Thanks for playing!')


