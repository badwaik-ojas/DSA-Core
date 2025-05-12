'''
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''

def all_unique(n):
    return len(n) == len(set(n))

seq = [1, 2, 5, 4, 6]
print(f"does this {seq} contains all unique values: ", all_unique(seq))

seq = [1, 2, 5, 4, 6, 4]
print(f"does this {seq} contains all unique values: ", all_unique(seq))
