from time import sleep
from alphabet import alphabet

class my_ascii_font:
    """Class that holds the variables and function definitions used by the My ASCII Font program.""" 
    
    def __init__(self, word="My ASCII Font", character='#', decoration=True, own_letter=False):
        """Function that initiates the instance variables and starts the program."""
        self.word = word # The word to be printed in the special font
        self.character = character # The character used as building block for creating the letters of the special font
        self.decoration = decoration # The Boolean variable that determines whether decoration is added to the print
        self.own_letter = own_letter # Boolean variable that determines whether each letter has itself as building block
        self.favorites = [] # List that holds that favorite creations of users
        self.welcome() # Function call that initiates the communication with the user

    def welcome(self):
        """Function executed at the start of the program."""
        self.print_word(self.word, self.character, self.decoration, self.own_letter) 
        print("\nWelcome to My ASCII Font.")
        self.decoration = False
        print("Enter your first name to see it typed in my font :)")        
        self.welcome_input()
        print("\nThe letters are made with the hash symbol. Want to replace it with something else? \
        \nChoose a single character of your choice and press enter.")
        self.character_input()
        self.decoration = True
        print("\nNice. Let's add some decoration to finalize your creation!\n")
        sleep(3)
        self.print_word(self.word, self.character, self.decoration, self.own_letter)
        print("\nNow you can make your own creation.")
        self.input_loop()
        
    def print_word(self, word, character, decoration, own_letter):
        """Function for printing the word entered by the user."""
        string_to_print = ''
        if decoration == True:
            print('\n*', end='')
            for letter in word:
                print('*' * len(alphabet[letter][0][0]), end='')
            print('***')        
        for i in range(11):
            for index in (range(len(word))):
                letter = word[index]
                if index == 0 and decoration == True:
                    if index == 0:
                        string_to_print += '* '
                if own_letter == False:
                    string_to_print += alphabet[letter][i][0].replace('#', character)
                if own_letter == True:
                    string_to_print += alphabet[letter][i][0].replace('#', letter)
                if index == len(word) -1 and decoration == True:
                    string_to_print += ' *'
            string_to_print += '\n'
        print(string_to_print, end= '')
        if decoration == True:
            print('*', end='')
            for letter in word:
                print('*' * len(alphabet[letter][0][0]), end='')
            print('***')

    def input_simple(self):
        """Function for taking user input."""
        return input()
    
    def welcome_input(self):
        """Function for word input only executed during the introduction."""
        word_input = '' 
        self.decoration = False
        correct = False
        while correct == False:
            word_input = self.input_simple()
            if not word_input:
                print("\nYou have not provided any input. Try again.")            
            else:
                correct = self.word_check(word_input)
                if correct == True:
                    self.word = word_input
                    self.print_word(self.word, self.character, self.decoration, self.own_letter)
    
    def word_check(self, word_input):
        """Function that validates the user input for word."""
        correct = True
        if len(word_input) > 15:
            print("\nThat's very long :( \nDo you have a shorter word for me?")
            correct = False
            return correct
        else:
            for letter in word_input:
                if letter not in alphabet:
                    print("\nYou have entered one or more characters I can't recognize :( \nTry again.")
                    correct = False
                    return correct
            return correct

    def character_input(self):
        """Function that validates the user input for character."""
        character_input = ''
        correct = False
        while correct == False:
            character_input = self.input_simple()
            if len(character_input) != 1:
                print("\nI only need a single character. Try again.")
                continue
            correct = True  
        self.character = character_input
        self.print_word(self.word, self.character, self.decoration, self.own_letter)
        
    def save_to_favorites(self):
        """Function that saves a creation to the favorites list."""
        self.favorites.append([self.word, self.character, self.decoration, self.own_letter])
            
    def show_favorites(self):
        """Function that prints the favorites list."""
        for i in range(len(self.favorites)):
            print("\n" + str(i + 1) + ')')
            self.print_word(self.favorites[i][0], self.favorites[i][1], self.favorites[i][2], self.favorites[i][3])
        
    def delete_favorites(self):
        """Function that deletes an item from the favorites list."""
        print("\nEnter -done to go back. If you want to remove an item, enter -remove x, with x representing the number of the item.") 
        done = False
        while done == False:
            word_input = self.input_simple()
            if not word_input:
                print("\nYou have not provided any input. Enter -remove x to remove an item or -done to go back.")            
            else:
                if word_input[0:7] == '-remove' and len(word_input) == 9:
                    if int(word_input[8]) in range(1,len(self.favorites) + 1):
                        self.favorites.pop(int(word_input[8]) - 1)
                        if len(self.favorites) > 0:
                            print("\nYour updated favorites list:")
                            self.show_favorites()
                            print("Item " + word_input[8] + " has been removed. Remove another one or enter -done to go back.")
                        else:
                            print("Your favorites list is now empty. Going back.")
                            done = True
                            sleep(2)
                    else:
                        print("Wrong input. Enter -remove x to remove an item or -done to go back.")
                elif word_input == '-done':
                    done = True
                else:
                    print("Wrong input. Enter -remove x to remove an item or -done to go back.")
                
    def input_loop(self):
        """Function that runs after the introduction has finished and continues to run until the user exits the program."""
        correct = False
        input_pass = False
        options = True
        instructions = "\nOptions:\
    \n-Enter a word if you want to see it printed.\
    \n-Enter -c to change the character that acts as building block of the font.\
    \n-Enter -d to add or remove the decoration.\
    \n-Enter -o to enable or disable the option of building each letter with itself.\
    \n-Enter -f to go to your favorites list.\
    \n-Enter -s to add your latest creation to your favorites list.\
    \n-Enter -quit to quit the program."
        while True:
            if options == True:
                options = False
                print(instructions)
            elif input_pass == False:
                print("\nEnter a word to have it printed or enter -help to see the available options.")
            input_pass = False
            input_temp = self.input_simple()
            if input_temp and input_temp[0] == '-':
                if len(input_temp) == 2:
                    if input_temp[1] == 'c':
                        self.own_letter = False
                        print("\nChoose a single character of your choice and press enter.")
                        self.character_input()   
                    elif input_temp[1] == 'd':
                        if self.decoration == True:
                            self.decoration = False
                        else:
                            self.decoration = True
                        self.print_word(self.word, self.character, self.decoration, self.own_letter)
                    elif input_temp[1] == 'o':
                        if self.own_letter == True:
                            self.own_letter = False
                        else:
                            self.own_letter = True
                        self.print_word(self.word, self.character, self.decoration, self.own_letter)
                    elif input_temp[1] == 'f':
                        if len(self.favorites) > 0:
                            print("\nThis is your favorites list:")
                            self.show_favorites()
                            self.delete_favorites()
                        else:
                            print("Your favorites list is still empty. To add your latest creation to it, enter -s.")
                            input_pass = True
                    elif input_temp[1] == 's':
                        if len(self.favorites) != 5:
                            self.save_to_favorites()
                            print("Your latest creation was saved to your favorites list! To view the list, enter -f.")
                            input_pass = True
                        else:
                            print("Unfortunately, your favorites list is full. Remove one or more items first from the favorites list.")
                            input_pass = True
                    else:
                        print("\nInvalid option. Enter -help to see the available options or try again.")
                        input_pass = True
                elif input_temp == '-quit':
                        exit()
                elif input_temp == '-help':
                        options = True
                        continue
                else:
                    print("\nInvalid option. Enter -help to see the available options or try again.")
                    input_pass = True
            elif len(input_temp) >= 1:
                correct = self.word_check(input_temp)
                if correct == False:
                    input_pass = True
                    continue
                self.word = input_temp
                self.print_word(self.word, self.character, self.decoration, self.own_letter)
            else:
                print("\nYou have not provided any input. Try again.")
                input_pass = True
                
instance = my_ascii_font()