'''
Created on Jan 8, 2021
String Functions
Narration: User selects one function to perform on a word or sentence. Over 10 Functions to choose from. Code breaks when user inputs name in characters from another language or in incorrect format.
Log 1.0: Initial version. Vowel/Consonant Count
Log 1.1: Added mode selection and lowercase/uppercase count function
Log 1.2: added loop 
Log 1.3: added all uppercase, all lowercase, space adder inbetween letters, and character counter.
Log 1.4: Added Shuffle and Reverse function
Log 1.5: Fixed bug with space adder. Got rid of global variable. Added palindrome check function.
Log 1.6: Added First Name. Documented Code
Log 1.7: Added middle name and last name, changed functions to return output back into the main.
Bugs: If user inputs their first and last name, the middle name function will return the last name
Bonuses: Loop, Uppercase Count, Lowercase Count, Space adder.
@author: apauley24
'''
'''
testing functions by sh:
everything works fine. No errors

'''
import random
#Sets up random functions




def main():

    '''
    This function is designed to ask the user for their input and lets them select from 14 functions to run
    :param: 
    :type name: 
    :returns:
    :raises
    '''

    loop_main = True                                                                                                #Loop so user can select multiple functions
    word = input("Input Word, Sentence, or your name(First Middle Last) > ")                                        #Sets up variable
    print("String Functions, Input number for each function")
    
    while loop_main == True:                                                                                        #Loop for selecting more options
        word_mode = input("[1] for vowel count. \n[2] for consonant count.\n[3] for uppercase count.\n[4] for lowercase count.\n[5] for space adder.\n[6] for all lowercase.\n[7] for all uppercase.\n[8] For counting a character.\n[9] for reversing your input.\n[10] for scrambling your input.\n[11] for checking if your input is a palindrome.\n[12] for first name.\n[13] for middle name.\n[14] for last name.")
        if word_mode == '1':
            vc = vowel_count(word)                                                                                  #Runs a function, and assigns a variable the returned output
            print("There are", vc, "vowels")
        elif word_mode == "2":
            cc = consonant_count(word)
            print("There are", cc, "consonants")
        elif word_mode == "3":
            uc_count = ucase_count(word)
            print(uc_count, "Uppercase Characters")
        elif word_mode == "4":
            lc_count = lcase_count(word)
            print(lc_count, "Lowercase Characters")
        elif word_mode == "5":
            space_word = space_adder(word)
            print(space_word)
        elif word_mode == "6":
            lc_word = lconly(word)
            print(lc_word)
        elif word_mode == "7":
            ucword = uconly(word)
            print(ucword)
        elif word_mode == "8":
            letter_counter = letter_count(word)
            print(letter_counter, "Characters of choice.")
        elif word_mode == "9":
            reverse_word = word_reverse(word)
            print(reverse_word)
        elif word_mode == "10":
            word_scrambled = shuffle_word(word)
            print(word_scrambled)
        elif word_mode == '11':
            if palindrome(word) == True:
                print("Your input is a Palindrome")
            elif palindrome(word) == False:
                print("Your input is not a Palindrome")
        elif word_mode == '12':
            name_first = first_name(word)
            print(name_first)
        elif word_mode == '13':
            name_middle = middle_name(word)
            print(name_middle)
        elif word_mode == '14':
            name_last = last_name(word)
            print(name_last)
            
    
                                                                                                                    #Elif block to ask user for function, run it, and print result.
            
        loop_input = input("Input 'Y' to run another function")
        if loop_input != 'Y' or loop_input != 'y':
            loop_main = False
            print("Done!")
        

def vowel_count(word):
    '''
    This function is designed to count the amount of vowels in the given word
    :param word: user input
    :type name: integer
    :type state:
    :returns: Returns the amount of vowels counted as an integer
    :raises
    '''
    vc = 0                                                                                                          #Sets up a variable to count the vowels.
    for letter in lconly(word):                                                                                            #Loop for each letter in word
        if letter == "e" or letter == "a" or letter == "i" or letter == "o" or letter == "u":
            vc = vc +1                                                                                              #Checks if the letter is a vowel, and adds one to the counter
    return vc                                                                                                       #sends the output back to the main


def consonant_count(word):
    '''
    This function is designed to count the amount of consonants in the given word
    :param word: user input
    :type name: string
    :type state:
    :returns: The amount of consonants counted as an integer
    :raises:
    '''
    cc = 0
    for letter in lconly(word):
        if letter != "e" and letter != "a" and letter != "i" and letter != "o" and letter != "u" and letter != ' ':
            cc = cc +1                                                                                              #Checks if the letter is not a vowel, and adds one to the counter if its a consonant
    return cc
    

def ucase_count(word):
    '''
    This function is designed to count the amount of uppercase characters.
    :param word: user input
    :type name: string
    :type state:
    :returns: The amount of uppercase characters counted as an integer
    :raises:
    '''
    uc_count = 0
    for letter in word:
        if ord(letter) >= 65 and ord(letter) <= 90:
            uc_count = uc_count + 1                                                                                 #Uses ASCII table to determine if letter is capital , then adds to the counter if it is. Uppercase characters are from 65 to 90
    return uc_count

def lcase_count(word):
    '''
    This function is designed to count the amount of lowercase characters.
    :param word: user input
    :type name: string
    :type state:
    :returns: The amount of lowercase characters counted as an integer
    :raises:
    '''
    lc_count = 0                                                                                                    #Sets up counting variable
    for letter in word:
        if ord(letter) >= 97 and ord(letter) <= 122:
            lc_count = lc_count + 1                                                                                 #Uses ASCII table to determine if letter is lowercase, then adds to the counter if it is. Lowercase characters are from 97 to 122
    return lc_count    
    
    
def space_adder(word):
    '''
    This function is designed to add spaces inbetween letters.
    :param word: user input
    :type name: string
    :type state:
    :returns: The new word with spaces added as a string.
    :raises: If the inputted amount of spaces is not able to be converted to an integer, it return an error message.
    '''
    space_word = ''                                                                                                  #Sets up a blank string so letters can be added
    space_amt = input("How many spaces between letters?")                                                            #Asks User for how many spaces they want inbetween
    try:                                                                                                            #Try and except to catch error by inputting any strings that can't work
        space_amt = int(space_amt)                                                                                    #Converts to integer to use in equation
        for letter in word:
            space_word = space_word + letter + ' ' * space_amt                                                         #Adds the letter to the new word then times the space my the amount inputted and adds it to the word
    except:
        print("Only Input positive integers.")                                                                      #Except to catch errors
    return space_word

def lconly(word):
    '''
    This function is designed to convert the word to all lowercase
    :param word: user input
    :type name: string
    :type state:
    :returns: The all lowercase word as a string
    :raises:
    '''
    lc_word = ''
    for letter in word:
        if ord(letter) <= 90 and ord(letter) >= 65:                                                                 #Sees if letter is an uppercase
            letter = ord(letter) +32                                                                                #Converts letter to ascii and adds 32 to convert to lowercase
            letter = chr(letter)                                                                                    #Converts the ASCII value back into a character
        lc_word = lc_word + str(letter)                                                                               #Adds it to the new word
    return lc_word
    
def uconly(word):
    '''
    This function is designed to convert the word to all uppercase
    :param word: user input
    :type name: string
    :type state:
    :returns: The all uppercase word as a string
    :raises:
    '''
    uc_word = ''
    for letter in word:
        if ord(letter) <= 122 and ord(letter) >= 97:                                                                #Checks if letter is a lowercase
            letter = ord(letter) - 32                                                                               #Subtracts 32 to turn it into a lowercase
            letter = chr(letter)
        uc_word = uc_word + str(letter)
    return uc_word
    
def letter_count(word):
    '''
    This function is designed to count the amount of a single character in a word
    :param word: user input
    :type name: string
    :type state:
    :returns: The amount of the character counted as an integer
    :raises:
    '''
    choice_letter = input("What character do you want to count?")                                                   #Asks user for the character they want to count
    if len(choice_letter) > 1:                                                                                      #if statement to check if the user input is longer than 1 character
        print("Please only input one letter or character")
    else:
        letter_counter = 0
        for letter in word:
            if letter == choice_letter:
                letter_counter = letter_counter + 1                                                                 #If the counted letter and the letter in the word are the same, adds one to the counter
    return letter_counter

def word_reverse(word):
    '''
    This function is designed to reverse the word
    :param word: user input
    :type name: string
    :type state:
    :returns: The new reversed word as a string
    :raises:
    '''
    reverse_word = ""
    for letter in range(len(word) -1, -1, -1):                                                                      #Runs the loop but in reverse from the end of the word in positions
        reverse_word = reverse_word + (word[letter])                                                                  #Converts the position to the letter in the word and adds it to the blank string
    return reverse_word
    
def shuffle_word(word):
    '''
    This function is designed to shuffle all the characters in the word
    :param word: user input
    :type name: string
    :type state:
    :returns: The shuffled word as a string
    :raises:
    '''
    word_scrambled = ''
    array_word = list(range(len(word)))                                                                              #Sets up a list of the positions in the word
    for letter in word:
        random_position = random.choice(array_word)                                                                   #Chooses a random positoin in the list
        array_word.remove(random_position)                                                                            #Removes the postion so it can't be chosen again so no duplicate letters
        word_scrambled = word_scrambled + word[random_position]                                                        #Converts the position to a letter and adds it to the blank string
    return word_scrambled

def palindrome(word):
    '''
    This function is designed to check if the word is a palindrome
    :param word: user input
    :type name: string
    :type state:
    :returns: True or false as a boolean.
    :raises:
    '''
    opplist = []                                                                                                    #Sets up a blank list
    for letter in range(len(word)):                                                                                 #Sets up a loop for each position in the word
        oppletter = len(word) - letter - 1                                                                          #Finds the opposite letter by subtracting the letters position and 1 to account for counting from 0
        oppletter = word[oppletter]                                                                                 #Converts the position of the opposite letter to the corresponding character in the word
        opplist.append(oppletter)                                                                                   #Adds the letter to the list
    if opplist == list(word):                                                                                       #Compares the list of opposite letters to a list of the letters in the word
        return True
    else:
        return False

def first_name(word):
    '''
    This function is designed to only take the first name
    :param word: user input
    :type name: string
    :type state:
    :returns: The first name as a string
    :raises:
    '''
    name_first = ''
    for letter in word:
        if letter == ' ':                                                                                           #Checks for the first space in name dividing the first name and middle/last name
            break                                                                                                   #Ends the loop
        else:
            name_first = name_first + letter                                                                        #If the character is not a space, adds it to the string and continues the loop#
    return name_first

def middle_name(word):
    '''
    This function is designed to only take the middle name
    :param word: user input
    :type name: string
    :type state:
    :returns: The middle name as a string
    :raises:
    '''
    space_counter = 0
    name_middle = ''
    for letter in word:
        if letter == ' ':
            space_counter = space_counter + 1                                                                       #Counts how many spaces to tell when the middle name is. The middle name is after the first space
        if space_counter == 1:                                                                                      #If there has been 1 space in the word, it starts adding the letters so it makes the middle name, once the name ends, there is a second space so it will stop adding letters
            name_middle = name_middle + letter
    return name_middle

def last_name(word):
    '''
    This function is designed to only take the last name
    :param word: user input
    :type name: string
    :type state:
    :returns: The last name as a string
    :raises:
    '''
    space_counter = 0
    name_last = ''
    for letter in word:
        if letter == ' ':
            space_counter = space_counter +1
        if space_counter == 2:                                                                                      #Starts counting the lastname after two spaces
            name_last = name_last + letter
            
    return name_last
        


            
            

        
if __name__ == "__main__":
    main()
    
    



    
    
    
    
