# File: BAITY013_encryptor.py
# Author: Tasha Bailey
# Stud Id: 110378613
# Email Id: baity013
# Description: Programming Assignment 2 - Caesar Cipher
# This is my own work as defined by the University's
# Academic Misconduct policy.

def get_offset():
    # Ask user for input
    offsetValue = int(input('Please enter offset value (1 to 94): '))

    # While the offset value has incorrect input
    while offsetValue <=0 or offsetValue >= 94:
        offsetValue = int(input('Please enter offset value (1 to 94): '))

    return offsetValue

    
def encrypt_string():
    # Ask user for input.
    print('\n')
    stringEncrypt = input('Please enter string to encrypt: ')
    
    # Call the function that asks for the offset value.
    offset = get_offset()
    encrypted = ''

    # For loop that loops through the individual letters in the message.
    for character in stringEncrypt:
        # Shift the character by the offset value.
        # 32 is the starting character
        # 95 + 32 = 126 is the end character
        encrypted = encrypted + chr((ord(character) + offset - 32) % 95 + 32)   

    # Display to user.
    print('\n')
    print('Encypted string:')
    print(encrypted)
    print('\n')
    
    return encrypted

def decrypt_string():
    # Ask user for input.
    print('\n')
    stringDecrypt = input('Please enter string to decrypt: ')

    # Call the function that asks for the offset value.
    offset = get_offset()
    decrypted = ''

    # For loop that loops through the individual letters in the message.
    for character in stringDecrypt:
    # Shift the character by the offset value.
    # Reverse the offset.
        # 32 is the starting character
        # 95 + 32 = 126 is the end character
        decrypted = decrypted + chr((ord(character) - offset - 32) % 95 + 32)

    # Display to user.
    print('\n')
    print('Decrypted string:')
    print(decrypted)
    
    return decrypted

def brute_force_decryption():
    # Ask user for input.
    stringDecrypt = input('Please enter string to decrypt: ')

    bruteForce = ''

    # Set offset value.
    offset = 1
    
    # For loop that loops through 94 possible offsets in the message.
    while offset != 95:
        for character in stringDecrypt:
            # Reverse the offset.
            # 32 is the starting character
            # 95 + 32 = 126 is the end character
            bruteForce = bruteForce + chr((ord(character) - offset - 32) % 95 + 32)

        print('Offset:', offset, 'Decrypted string: ', bruteForce)
        offset = offset + 1
        bruteForce = ''
        
    return bruteForce


def get_menu_choice():
    # Prompt for user to choose options from the menu.
    print('\n')
    print('*** Menu ***')

    print('1. Encrypt string')
    print('2. Decrypt string')
    print('3. Brute force decryption')
    print('4. Quit')

    # Prompt user to choose the option they want.
    print('\n')
    userChoice = int(input('What would you like to do [1, 2, 3, 4]? '))

    while userChoice != 4:
        # While the user inputs any other character
        while userChoice != 1 and userChoice != 2 and userChoice != 3  and userChoice != 4:
            print('Invalid choice, please enter either 1, 2, 3 or 4.')

            # Prompt user to choice the option they want.
            print('\n')
            userChoice = int(input('What would you like to do [1, 2, 3, 4]? '))
            
        # Logic - if statement

        # If the user choose 1
        if userChoice == 1:
            # Call function that encrypts the string.
            encrypt_string()

            # Prompt for user to choose options from the menu.

            print('*** Menu ***')

            print('1. Encrypt string')
            print('2. Decrypt string')
            print('3. Brute force decryption')
            print('4. Quit')
            print('\n')
            
            # Prompt user to choose the option they want.

            userChoice = int(input('What would you like to do [1, 2, 3, 4]? '))
            
        # If the user choose 2
        elif userChoice == 2:
            # Call function that decrypts the string.
            decrypt_string()

            # Prompt user to choose the option they want.

            # Prompt for user to choose options from the menu.
            print('\n')
            print('*** Menu ***')

            print('1. Encrypt string')
            print('2. Decrypt string')
            print('3. Brute force decryption')
            print('4. Quit')
            print('\n')
            
            userChoice = int(input('What would you like to do [1, 2, 3, 4]? '))
            
        # If the user choose 3
        elif userChoice == 3:
            # Prompt for user to choose options from the menu.

            # Call function that uses a brute force decrytion.
            brute_force_decryption()

            # Prompt for user to choose options from the menu.
            print('\n')
            print('*** Menu ***')

            print('1. Encrypt string')
            print('2. Decrypt string')
            print('3. Brute force decryption')
            print('4. Quit')
            print('\n')
            
            # Prompt user to choice the option they want.
            userChoice = int(input('What would you like to do [1, 2, 3, 4]? '))

        # If the user chooses 4
        else:
            # The reason for the pass statement is if the user inputs 5, and then corrects it
            # to 4, if there is another print('Goodbye.') statement, it will execute twice.
            pass
            
def display_details():
    # Display author details to user.
    print('File: BAITY013_encryptor.py')
    print('Author: Tasha Bailey')
    print('Stud ID: 110378613')
    print('Descryption: Programming Assignment 2 - Caesar Cipher')
    print('This is my own work as defined by the University\'s Academic Misconduct Policy. \n')

# Call function to display details.
display_details()

# Call function that handles the menu.
get_menu_choice()

# If the user chooses 4
print('\n')
print('Goodbye.')


 
