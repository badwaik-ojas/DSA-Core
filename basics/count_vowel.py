'''
Write a short Python function that counts the number of vowels in a given
character string.
'''

def count_vowels(s):
    vowels = 'AEIOU'
    count = sum(1 for x in s.upper() if x in vowels)
    return count

str = "hello, I am Ojas"

print(f"vowel count in given string: {str} = ", count_vowels(str))