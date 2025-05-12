'''
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''

def is_even(n):
    return (n & 1) == 0

print("Is 14 even? ", is_even(14))
print("Is 29 even? ", is_even(29))
