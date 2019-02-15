numbers = [1, 7, 5, 3, 10, 10, 12, 12, 10]

# finds the largest number in a list


def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if largest <= num:
            largest = num
    print(largest)


find_largest(numbers)
