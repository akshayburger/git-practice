while True:
    print("--------------------------------")
    print("Welcome to the calculator")
    print("--------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sum = a + b
        print("The sum of the two numbers is: ", sum)
    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        difference = a - b
        print("The difference of the two numbers is: ", difference)
    elif choice == 3:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        product = a * b
        print("The product of the two numbers is: ", product)
    elif choice == 4:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if b == 0:
            print("Error: Division by zero")
            continue
        quotient = a / b
        print("The quotient of the two numbers is: ", quotient)
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        continue
    print("--------------------------------")
    print("Thank you for using the calculator")
    print("--------------------------------")
    print("Do you want to continue? (y/n)")
    choice = input("Enter your choice: ")
    if choice == "n":
        break
    else:
        continue





