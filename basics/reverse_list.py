'''
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''

def reverse_list(l):
    n = len(l)
    for x in range(n//2):
        l[x], l[n-1-x] = l[n-1-x], l[x]
    return l

l1 = [2, 4, 5, 1, 3, 0]
print(f" reverse of {l1}: ", reverse_list(l1))

# with built-in function
l1 = [2, 4, 5, 1, 3, 0]
print(f" reverse of {l1} with built in function: ", l1[::-1])

'''
🔁 Comparison
Feature	                Pseudo-code / Manual Python	    Python Slice Method ([::-1])
In-place reversal	    ✅ Yes                         ❌ No (returns new list)
Simplicity	            Moderate	                    Very simple
Performance	            O(n)	                        O(n)
Memory efficiency	    High (in-place)	                Uses extra memory
'''


