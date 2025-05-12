'''
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once
'''

import itertools

def generate_permutations():
    chars = ['c', 'a', 't', 'd', 'o', 'g']
    all_permutations = itertools.permutations(chars)
    count = 0
    for p in all_permutations:
        print(''.join(p))
        count +=1
    print(count)

generate_permutations()

'''
with recursion
'''

def generate_permutations_1(chars, prefix=''):
    if len(chars)==0:
        print(prefix)
    else:
        for i in range(len(chars)):
            new_prefix = prefix + chars[i]
            remaining = chars[:i] + chars[i+1:]
            generate_permutations_1(remaining, new_prefix)

generate_permutations_1("catdog")

