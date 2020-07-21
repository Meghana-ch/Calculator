# A mini calculator program
# Ask the user to choose whether what kind of operation do they want to perform on 2 numbers? i.e. add, multiply, subtract or divide
# Next, prompt the user to enter 2 numbers and store these two numbers
# Based on what operation the user chose, send those two numbers to the respective function. Perform the operation
# and then return the output to be printed into the console

def add(x, y):
    return [x + y]
def sub(x, y):
    return[x - y]
def multi(x, y):
    return[x * y]
def div(x, y):
    return[x/y]

print("What kind of operation would you like to perform? please enter the first letter.\n\n\n\n\n")
print("Add? - A")
print("Subtract? - S")
print("Multiply? - M")
print("Divide? - D")

while True:
    choice = input("Enter choice(A/S/M/D): ")
    if choice in ('A', 'S', 'M', 'D'):
        num1, num2 = list(map(float, input("PLease enter two numbers: ").split()))

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'S':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == 'M':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", div(num1, num2))
        break
    else:
        print("Invalid Input")