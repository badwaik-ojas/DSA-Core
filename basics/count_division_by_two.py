'''
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''

def count_division_by_two(n):
    if n <=2:
        ValueError("please enter value greater than 2")
        return 
    
    i = n
    count = 0
    while i >= 2:
        count +=1
        i = i//2
    return count

value =  int(input("Enter value greater than 2: "))

print("number of values divided by 2: ", count_division_by_two(value))
