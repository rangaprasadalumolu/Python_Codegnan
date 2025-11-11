import add
import sub as sb
from mul import multiplication
from div import division

# main
if __name__ == "__main__":
    print("Welcome to Simple Calculator")
    operations = (
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Exit\n"
    )
    print(operations)

    while True:
        choice = int(input("Enter your operation: "))

        if choice == 1:
            x, y = map(int, input("Enter two numbers: ").split())
            res = add.addition(a=x, b=y)
            print("Result:", res)

        elif choice == 2:
            x, y = map(int, input("Enter two numbers: ").split())
            res = sb.subtraction(a=x, b=y)
            print("Result:", res)

        elif choice == 3:
            x, y = map(int, input("Enter two numbers: ").split())
            res = multiplication(a=x, b=y)
            print("Result:", res)

        elif choice == 4:
            x, y = map(int, input("Enter two numbers: ").split())
            res = division(a=x, b=y)
            print("Result:", res)

        elif choice == 5:
            print("Exiting Calculator. Goodbye!")
            break

        else:
            print("Select correct Operation")
