input_1 = int(input("Enter first number: "))
input_2 = input("Enter operand: ")
input_3 = int(input("Enter second number: "))


def add(input_1, input_2):
    result = input_1 + input_2
    return result


def subtract(input_1, input_2):
    result = input_1 - input_2
    return result


def multiply(input_1, input_2):
    result = input_1 * input_2
    return result


def divide(input_1, input_2):
    result = input_1 / input_2
    return result


def what_operation(input_2):
    if input_2 == "+":
        final_result = add(input_1, input_3)
    elif input_2 == "-":
        final_result = subtract(input_1, input_3)
    elif input_2 == "*":
        final_result = multiply(input_1, input_3)
    else:
        final_result = divide(input_1, input_3)
    return final_result


answer = what_operation(input_2)
print(answer)
