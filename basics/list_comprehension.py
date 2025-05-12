'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
'''

result = [i * (i + 1) for i in range(10)]
print(result)

'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally

✅ Explanation:
ord('a') gives the ASCII value of 'a' (97)
ord('z') gives the ASCII value of 'z' (122)
chr(i) converts an ASCII value back to a character
'''
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(alphabet)


