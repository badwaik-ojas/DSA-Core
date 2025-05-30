'''
Give an example of a Python code fragment that attempts to write an element
to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
'''

def write_to_list(list, index, value):
    try:
        list[index] = value
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")

list = [1, 2, 3]
print("add an element to 5 index with value 10: ", write_to_list(list, 5, 10))