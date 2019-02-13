print("This app will calculate the factorial of any number you enter.")

number = int(input("Please enter a number: "))


def factorial(num):
    numbers = []
    fact = 1
    while num > 0:
        numbers.append(num)
        num -= 1
    for i in range(0, len(numbers)):
        fact *= numbers[i]

    print(fact)


factorial(number)

# ----- A much easier way Sebastian G. showed me ------
#fact_2 = 1
# for i in range(1, number + 1):
#    fact_2 *= i
# print(fact_2)
