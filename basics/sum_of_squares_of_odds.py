'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''

def sum_of_squares_of_odds(n):
    return sum(x*x for x in range(1,n,2))

print("sum of square of odd numbers till n: ", sum_of_squares_of_odds(5))