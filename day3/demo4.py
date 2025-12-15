def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
num1=("enter 1st number:")
num2=("enter 2nd number:")

while True:
    print("\n Arithmetic Operations Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting program...")
        break

    num1 = float(input("Enter first number: "))
    num2= float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
            print("Result:",sub(num1,num2))
    elif choice==3:
        print("Result:",mul(num1.num2))
    elif choice==4:
        print("Result:",div(num1,num2))
    else:
        print("Invalid choice! Please try again.")