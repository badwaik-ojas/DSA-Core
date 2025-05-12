'''
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?
'''

'''
j = n + k
Negative index k counts backward from the end.

Adding the length n shifts it to the equivalent positive index.

'''
s = "hello"  # length = 5
k = -2
j = len(s) + k
print(s[k])  # 'l'
print(s[j])  # also 'l'
