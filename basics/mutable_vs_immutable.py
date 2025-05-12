'''
Understanding the Function:

def scale(data, factor):
    for j in range(len(data)):
        data[j] = factor

Key Concepts:
data is typically a mutable sequence, like a list.
Numeric values (factor, data[j], etc.) are immutable — changing them creates a new number object.
However, lists themselves are mutable — their contents can be changed.

So why does data[j] = factor change the caller's list?
Because:

data is a reference to the original list passed in.

data[j] = factor modifies the list container, replacing an element at index j with a new number.

You're not modifying the number itself (which is immutable), you're mutating the list by assigning a new value at that position.

Analogy:
Think of a list like a row of mailboxes:

You’re not changing the letter (int) inside the mailbox (list index) — you're replacing it with a new letter.

The mailbox structure (list) remains the same — you're just putting different contents in.

Example:

lst = [1, 2, 3]
scale(lst, 5)
print(lst)  # Output: [5, 5, 5]

Despite int being immutable, the list was mutated, because its elements were reassigned.

'''