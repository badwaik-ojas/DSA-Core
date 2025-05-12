'''
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''

def has_odd_product_pair(seq):
    odd_count = sum(1 for x in seq if x%2 != 0)
    return odd_count >=2

seq  = [1, 3,4,5,6,10]
print("does the list contains distinct pairs of integer whose product is odd: ", has_odd_product_pair(seq))

seq  = [1, 2,4,4,6,10]
print("does the list contains distinct pairs of integer whose product is odd: ", has_odd_product_pair(seq))

