'''
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
'''

def make_change(amount_charged, amount_given):
    if amount_given < amount_charged:
        print("Amount given is less than the amount charged. No change.")
        return

    change = round((amount_given - amount_charged) * 100)  # Convert to cents
    print(f"Total change to give back: ${change / 100:.2f}")

    denominations = {
        "100 dollar bill": 10000,
        "50 dollar bill": 5000,
        "20 dollar bill": 2000,
        "10 dollar bill": 1000,
        "5 dollar bill": 500,
        "1 dollar bill": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1,
    }

    for name, value in denominations.items():
        count = change // value
        if count > 0:
            print(f"{count} x {name}{'s' if count > 1 else ''}")
            change %= value

# Example usage:
charged = float(input("Enter the amount charged: $"))
given = float(input("Enter the amount given: $"))
make_change(charged, given)
