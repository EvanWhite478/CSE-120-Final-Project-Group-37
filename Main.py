from functions import *

while True:
    menu()
    user_input = input(": ")
    if user_input == "11":
        break
    elif user_input in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            result = add(num1, num2)
        elif user_input == "2":
            result = subtract(num1, num2)
        elif user_input == "3":
            result = multiply(num1, num2)
        elif user_input == "4":
            result = divide(num1, num2)
        print("Result: " + str(result))
        print()

    elif user_input == "5":
        print(sqrt_root())
        print()
    elif user_input == "6":
        print(logarithmic())
        print()
    elif user_input == "7":
        print(log2())
        print()
    elif user_input == "8":
        print(exp())
        print()
    elif user_input == "9":
        print(fact())
        print()
    
    if user_input == "10" :
        print()
        specialFunctionsMenu()
        special_user_input = input(": ")
        if special_user_input == "1":
            print(bsc_derivatives())
            print()
        elif special_user_input == "2":
            print(quadratic_formula())
            print()
        elif special_user_input == "3":
            print(gcd())
            print()
        elif special_user_input == "4":
            print(plot_equation())
            print()
        elif special_user_input == "5":
            geometric_menu()
            print()
        else:
            print("the value is not included, please try again")
