# try:
#     result=10/0
#
# except ZeroDivisionError:
#     print("Opps! Tried to divide by zero!")
#
#
#     fruits = {
#         "apple" : 5,
#         "orange" : 3,
#         "banana": 7
# }
# try:
#  print(fruits["cherry"])
#
# except KeyError :
#  print("The key does not match in the dictionary")
#
#
#  text = "This is not a number"
#
# try:
#      text_to_int = int(text)
#
# except Exception as e:
#      print("An error occurred", e)
#
# try:
#      result = 10/2
# except ZeroDivisionError:
#     print("Division by 0")
# else:
#     print("Division succsesful. Result = ", result)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("We have an error, we cant devide by 0")
# finally:
#     print("Finally block executed")
#
# def divide_numbers(a,b):
#     try:
#         result = a/b
#         print("The result is:", result)
#     except ZeroDivisionError:
#         print("You tried to divide by 0")
#     except TypeError:
#         print("Invalid type for division")
#     except Exception as e:
#         print("Unexpected error", e)
#     else:
#         print("The result is: ", result)
#
# divide_numbers(10,2)
# divide_numbers(10,0)
# divide_numbers(10,'2')


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        raise ValueError("Invalid operation.")


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    op = input("Enter an arithmetic operator (+, -, *, /): ")

    result = calculate(num1, num2, op)

    print("Result:", result)

except ValueError as ve:
    print("ValueError:", ve)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program has ended.")

