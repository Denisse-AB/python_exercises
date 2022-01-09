'''
Find the average length in the sentence
'''
import statistics
import math

word = "The longest word in the dictionary is..."

array = []

def average_len(word):
    char = "[@_!#$%^&.,;*()<>?/|}{~:`]"
    remove = word.translate({ord(i): None for i in char})
    spl = remove.split()

    for i in spl:
      length = len(i)
      array.append(length)

average_len(word)

static = statistics.mean(array)
print(math.ceil(static))
