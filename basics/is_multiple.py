'''
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

def is_multiple(n, m):
    return n%m == 0

print("2 is multiple of 4? ", is_multiple(4, 2))
print("3 is multiple of 8? ", is_multiple(8, 3))