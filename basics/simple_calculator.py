'''
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
'''

def simple_calculator():

    print("Simple Calculator(type 'exit' to quit)")
    total = None
    operator = None

    while True:
        user_input = input(">>> ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("Exiting Calculator...")
            break

        try:
            num = float(user_input)
            if total is None:
                total = num
            elif operator:
                if operator == '+':
                    total += num
                elif operator == '-':
                    total -= num
                elif operator == '*':
                    total *= num
                elif operator == '/':
                    if num == 0:
                        print("Error. Division by 0")
                        continue
                    total /=num
                operator = None
                print("Display: ", total)
        except ValueError:
            if user_input in ['+', '-', '*', '/']:
                operator = user_input
            elif user_input == '=':
                print("Total: ", total)
                total = None
            else:
                print("Invalid input. please enter a number or an operator(+, -, /, *)")

simple_calculator()
            


            
