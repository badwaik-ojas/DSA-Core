'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

with loop
'''

def sum_of_squares_loop(n):
    sum = 0
    for x in range(1, n):
        sum = sum + x*x
    return sum

print("sum of squares of numbers till 5 ", sum_of_squares_loop(5))
print("sum of squares of numbers till 3 ", sum_of_squares_loop(3))