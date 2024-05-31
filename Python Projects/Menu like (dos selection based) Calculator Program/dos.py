while True:
    # Display the menu
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    # Get user choice
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        # Addition
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        result = a + b
        print(f"The result is {result}")
    
    elif choice == '2':
        # Subtraction
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        result = a - b
        print(f"The result is {result}")
    
    elif choice == '3':
        # Multiplication
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        result = a * b
        print(f"The result is {result}")
    
    elif choice == '4':
        # Division
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        if b == 0:
            print("Error: Division by zero")
        else:
            result = a / b
            print(f"The result is {result}")
    
    elif choice == '5':
        # Exit
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice, please choose a number between 1 and 5.")
    
    # Wait for the user to press any key to continue
    input("Press any key to continue...")

    # Print a new line for better readability in the next iteration
    print()
