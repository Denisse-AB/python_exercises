'''
Replace every letter with a backwards version of the alphabet.
'''
import string

word = 'Hello World'.lower()

letters = string.ascii_lowercase

mytable = word.maketrans(letters, letters[::-1])
print(word.translate(mytable))
