from functions import *

while True:
    # Displays menu
    menu()
    # Gathers the user's action
    user_input = input(": ")
    # Stops the calculator if the input is '11'
    if user_input == "11":
        break
    # Requests two numbers if the user input is in the range 1 to 4
    elif user_input in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            # Passes the requested numbers to be added
            result = add(num1, num2)
        elif user_input == "2":
            # Passes the requested numbers to be subtracted
            result = subtract(num1, num2)
        elif user_input == "3":
            # Passes the requested numbers to be multiplied
            result = multiply(num1, num2)
        elif user_input == "4":
            # Passes the requested numbers to be divided
            result = divide(num1, num2)
        # Prints result and space
        print("Result: " + str(result))
        print()

    
    elif user_input == "5":
        # Prints square root result
        print(sqrt_root())
        print()
    elif user_input == "6":
        # Prints log
        print(logarithmic())
        print()
    elif user_input == "7":
        # Prints log base 2
        print(log2())
        print()
    elif user_input == "8":
        # Prints exponent
        print(exp())
        print()
    elif user_input == "9":
        # Prints factorization
        print(fact())
        print()
    
    if user_input == "10" :
        print()
        # Displays special functions menu
        specialFunctionsMenu()
        special_user_input = input(": ")
        if special_user_input == "1":
            # Prints derivatives
            print(bsc_derivatives())
            print()
        elif special_user_input == "2":
            # Prints values of quadratic formula
            print(quadratic_formula())
            print()
        elif special_user_input == "3":
            # Prints gcd
            print(gcd())
            print()
        elif special_user_input == "4":
            # Shows the plot of an equation
            print(plot_equation())
            print()
        elif special_user_input == "5":
            # Shows the geometric menu and displays the result after an user has choosen its path
            geometric_menu()
            print()
        else:
            # The value is outside the code, goes back to the beginning
            print("the value is not included, please try again")
