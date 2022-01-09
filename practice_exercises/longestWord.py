'''
Find the longest word
'''
txt = "Quisque quis eros sed elit ultrices dignissim nec in elit. Nam eu dui vel dui lobortis rutrum at non odio.Phasellus molestie, velit a rhoncus finibus, nisi turpis ornare enim, non convallis tellus erat at enim. Vivamus gravida laoreet ligula non euismod."

#your code goes here
find = txt.split()
longest_word = max(find, key=len)
print(longest_word)