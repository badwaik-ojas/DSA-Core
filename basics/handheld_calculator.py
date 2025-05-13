'''
Write a Python program that simulates a handheld calculator. Your program
should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation
is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
'''

def handheld_calculator():
    print("Handheld Calculator (enter 'exit' to quit)...")
    current = 0
    operator = None
    waiting_for_number = True

    while True:
        user_input = input(">>> ").strip()

        if user_input in ['exit', 'quit']:
            print('Exiting Calculator...')
            break

        if user_input in ['+', '-', '*', '/']:
            operator = user_input
            waiting_for_number = True
            continue

        if user_input.upper() == 'C':
            current = 0
            operator = None
            waiting_for_number = True
            print("Memory cleared...")
            continue

        if user_input == '=':
            print("Total: ",current)
            continue

        try: 
            num = float(user_input)
            if operator and waiting_for_number is False:
                if operator == '+':
                    current +=num
                elif operator == '-':
                    current -=num
                elif operator == '*':
                    current *=num
                elif operator == '/':
                    if num == 0:
                        print("Division by 0 Error")
                        continue
                    current /=num
                print("Total: ", current)
                operator = None
            else:
                if operator is None:
                    current = num
                if operator == '+':
                    current +=num
                elif operator == '-':
                    current -=num
                elif operator == '*':
                    current *=num
                elif operator == '/':
                    if num == 0:
                        print("Division by 0 Error")
                        continue
                    current /=num
                print("Total: ", current)
                operator = None
            waiting_for_number = False
        except ValueError:
            print("Please enter a valid number or an operator among the defined values(+, -, *, /, =, C)")
                
handheld_calculator()