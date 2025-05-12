'''
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
'''

import string

#print(string.punctuation)
def remove_punctuation(str):
    s = ''.join([s for s in str if s not in string.punctuation])
    return s

str = "Let s try, Mike."

print("String without punctuation: ", remove_punctuation(str))