import math

print("\nCalculator\n")
i = 0
while i < 1:
    print("\nPlease select operation:\n")
    print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Power\n 6. Quit\n")

    choice = int(input("\nSelect operations:"))

    if choice != 6:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", num1, "+", num2,
                  "=", str(num1 + num2))

        elif choice == 2:
            print("Result:", num1, "-", num2,
                  "=", str(num1 - num2))

        elif choice == 3:
            print("Result:", num1, "*", num2,
                  "=",  str(num1 * num2))

        elif choice == 4:
            print("Result:", num1, "/", num2,
                  "=", str(num1 / num2))
        elif choice == 5:
            print("Result:", num1, "^", num2, "=", str(num1 ** num2))
        else:
            print("Invalid input. Please enter again.")

    else:
        i = i + 1
        print('\nThank You for using my Program!!')
        break
