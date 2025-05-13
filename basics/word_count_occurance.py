'''
Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.

✅ Features:

Uses input() to read a line of text
Splits the input into words using whitespace
Counts each word using a dictionary
'''

def count_word_occurance():
    in1 = input("Please enter text here: ")

    words = in1.lower().split(" ")
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    for key, value in word_count.items():
        print(f"{key}: {value}")

count_word_occurance()
