'''
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
'''

def check_arithmetic_formula(a, b, c):
    if a+b == c:
        print(f"{a} + {b} = {c}")
    elif a == b-c:
        print(f"{a} = {b} - {c}")
    elif a*b == c:
        print(f"{a} * {b} = {c}")
    else:
        print("No valid arithmetic formula found")
    
a = int(input("Input value for a: "))
b = int(input("Input value for b: "))
c = int(input("Input value for c: "))

print("the formula that matched: ", check_arithmetic_formula(a, b, c))