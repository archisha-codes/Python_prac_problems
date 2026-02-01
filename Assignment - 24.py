# ============================================================
# Assignment 24 : Python Exception Handling
# ============================================================


# ------------------------------------------------------------
# 1. Write a python script to create an ArithmeticError
# ------------------------------------------------------------
print("\nQ1: Create an ArithmeticError")

try:
    a = 10 / 0
except ArithmeticError as e:
    print("ArithmeticError created:", e)



# ------------------------------------------------------------
# 2. Write a python script to create a ValueError
# ------------------------------------------------------------
print("\nQ2: Create a ValueError")

try:
    num = int("abc")
except ValueError as e:
    print("ValueError created:", e)


# ------------------------------------------------------------
# 3. Write a python script to handle the ArithmeticError
# ------------------------------------------------------------
print("\nQ3: Handle ArithmeticError")

try:
    x = 10 / 0
except ArithmeticError:
    print("ArithmeticError handled successfully")



# ------------------------------------------------------------
# 4. Write a python script to handle the ValueError
# ------------------------------------------------------------
print("\nQ4: Handle ValueError")

try:
    num = int("xyz")
except ValueError:
    print("ValueError handled successfully")



# ------------------------------------------------------------
# 5. Write a python script to handle multiple exceptions
#    in one try block
# ------------------------------------------------------------
print("\nQ5: Handle multiple exceptions")

try:
    a = int("abc")
    b = 10 / 0
except (ValueError, ArithmeticError) as e:
    print("Exception handled:", type(e).__name__)



# ------------------------------------------------------------
# 6. Write a python script to create a calculator with
#    4 basic operations and handle maximum exceptions
# ------------------------------------------------------------
print("\nQ6: Calculator with exception handling")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        raise ValueError("Invalid operator")

except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError as ve:
    print("Value Error:", ve)
except Exception as e:
    print("Unexpected Error:", e)



# ------------------------------------------------------------
# 7. Write a python script to add a finally block
#    for the above script
# ------------------------------------------------------------
print("\nQ7: Calculator with finally block")

try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print("Division:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed (finally block)")



# ------------------------------------------------------------
# 8. Write a python script to implement try, except
#    and else block for division
# ------------------------------------------------------------
print("\nQ8: try-except-else for division")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Division by zero error")
else:
    print("Division result:", result)



# ------------------------------------------------------------
# 9. Write a python script to raise a ValueError
# ------------------------------------------------------------
print("\nQ9: Raise a ValueError")

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is valid")
except ValueError as e:
    print("Error:", e)



# ------------------------------------------------------------
# 10. Write a python script to implement nested try-except
# ------------------------------------------------------------
print("\nQ10: Nested Try-Except")

try:
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Inner except: Cannot divide by zero")
except ValueError:
    print("Outer except: Invalid input")