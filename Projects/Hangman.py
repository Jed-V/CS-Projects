#Hangman.py
import string
import sys
import random
def main():
    
    word = ""
    letters guessed = []
    alphabet = list(string.ascii_lowercase)
    word_list = ['LYNX', 'ZEPHYR', 'ALBATROSS', 'CHEETAH', 'DIPOLE', 'CATACLYSM', 'BIOMOLECULAR'\
                'DOPAMINE', 'LICORICE', 'CRAYON', 'BONELESS', 'HEIGHT']
    
    print("Welcome to Hangman!\n")
    game_over = False
    while (not game_over):
        word = input("Would you like to enter your own word? [y/n]\n")
        
        if type(word) == str and word.upper == "Y":
            word = input("Enter word here: \n")
        else:
            a = random.randint(1, len(word_list)-1)
            word = word_list[a]
        done = False   
        while (not done):
            print('Word: \n')
            for i in range(len(word)):
                print('_')
            
            done = True
def check_latter(let, user_word):
    if let.upper in alphabet:
        if 










