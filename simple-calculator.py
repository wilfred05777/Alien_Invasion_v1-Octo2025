# Simple CLI Calculator

print("This is a basic caculator program")
print("**Select desired Operations")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")

choices = input("Enter choice 1/2/3/4: ")

# Keep asking until a valid choice is made
while True:
    choices = input("Enter choice (1/2/3/4): ")
    if choices in ('1', '2', '3', '4'):
        break
    else:
        print("⚠️ Invalid choice. Please select a proper number (1-4) to proceed.\n")

# while True:
#     choice = input("Enter choice (1/2/3/4): ")
    
#     if choice == '1' or choice == '2' or choice == '3' or choice == '4':
#         print("Valid choice! Proceeding...\n")
#         break
#     else:
#         print("⚠️ Invalid choice. Please select a proper number (1-4) to proceed.\n")
    
a = float(input("Input first number: "))
b = float(input("Input second number: "))


if(choices == '1'):
    result = a + b
    print(f" Addition result is: {result}")

else:
    print("Invalid choices! you must select a valid operation")
    



# print("Welcome to the Python Calculator!")
# print("Select operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# # Ask the user to select an operation
# choice = input("Enter choice (1/2/3/4): ")

# # Ask for two numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Perform the selected operation
# if choice == '1':
#     result = num1 + num2
#     print(f"The result of addition is: {result}")
# elif choice == '2':
#     result = num1 - num2
#     print(f"The result of subtraction is: {result}")
# elif choice == '3':
#     result = num1 * num2
#     print(f"The result of multiplication is: {result}")
# elif choice == '4':
#     if num2 != 0:
#         result = num1 / num2
#         print(f"The result of division is: {result}")
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid input. Please choose a valid operation (1-4).")
