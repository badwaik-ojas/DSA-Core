'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

with for comprehension
'''

def sum_of_squares(n):
    return sum(x*x for x in range(1, n))

print("sum of squares of numbers till 5 ", sum_of_squares(5))
print("sum of squares of numbers till 3 ", sum_of_squares(3))