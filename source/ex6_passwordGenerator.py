# Password generator
import random
from time import sleep
import string

def gen_pass(lenght):
    '''
    We are defining a function which will generate a password out of the main printable character set.
    The input of the function is a number bigger than 8
    '''
    # We define a char_set adding all the letters (upper and lower case), number and punctuation signs.
    char_set = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(lenght):
        password += random.choice(char_set) # Get iteratively from the char_set in a random way
    return password


def main():
    '''
    Function to run this program. It will ask for a number until it's bigger or equal to 8.
    '''
    running = True
    while running:
        pass_len = int(input('introduce desired lenght for your new password (min 8 characters): '))
        if pass_len >= 8:
            new_password = gen_pass(pass_len)
            print('Your new password is: ',new_password)
            running = False
        elif pass_len < 8:
            print('Minimum lenght for a password is 8 characters')
            sleep(2)


main() # Run this program
