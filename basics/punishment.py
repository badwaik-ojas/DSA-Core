'''
A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.

Here is a stand-alone Python program that prints the sentence:

“I will never spam my friends again.”
It prints it 100 times, each numbered.
It introduces 8 random-looking typos across the 100 lines.

Introduces 8 typos at random lines

Typos include:
Missing characters
Repeated characters
Swapped characters
Wrong character inserted


'''

import random

def make_typo(sentence):
    typo_type = random.choice(['missing', 'duplicate', 'swap', 'wrong'])
    idx = random.randint(0, len(sentence)-2)

    if typo_type == 'missing':
        return sentence[:idx] + sentence[idx+1:]
    if typo_type == 'duplicate':
        return sentence[:idx] + sentence[idx] + sentence[idx] + sentence[idx+1:]
    if typo_type == 'swap':
        return sentence[:idx] + sentence[idx+1] + sentence[idx] + sentence[idx+2:]
    if typo_type == 'wrong':
        wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        return sentence[:idx] + wrong_char + sentence[idx+1:]
    
    return sentence

def punishment():
    sentence = "I will never spam my friends again."
    typo_lines = set(random.sample(range(1, 101), 8))

    for i in range(1, 101):
        current_sentence = sentence
        if i in typo_lines:
            current_sentence = make_typo(sentence)
        print(f'{i}. {current_sentence}')

punishment()
    
