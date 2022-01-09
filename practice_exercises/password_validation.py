'''
Password validator, more than 7 characters long
at least 2 characters, 2 numbers and an upper letter
'''

import re, string

char = string.punctuation

inp = '2Hello*world!0'

password = inp.strip().replace(' ', '')

def valid_pass(password, char):
    if len(password) <= 7 or re.search(r"[A-Z]", password) == None:
       print('Weak')
       return

    numbers = [num for num in password if num.isdigit()]

    if len(numbers) < 2:
        print('Weak')
        return

    characters = [caract for caract in char if caract in password]

    print('Weak') if len(characters) < 2 else print('Strong')

valid_pass(password, char)
