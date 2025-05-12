'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''

def minmax(data):
    smallest = largest = data[0]
    for val in data[1:]:
        if val < smallest:
            smallest = val
        if val > largest:
            largest = val
    return smallest, largest

l = [2,3,1,4,5,0]
print(f"minmax of {l}: ", minmax(l))

l1 = [100, 455, 3,-4, 100, 744]
print(f"minmax of {l1}: ", minmax(l1))
