
number = int(input("Please enter a number: "))


def is_prime(num):
    if num == 1 or num == 2:
        result = True
        return result
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
        else:
            result = True
    return result


answer = is_prime(number)

if answer == True:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a not a prime number.")
