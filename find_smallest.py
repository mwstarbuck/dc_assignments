numbers = [10, 7, 5, 3, 3, 2, 5]

# finds the smallest number in a list


def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if smallest >= num:
            smallest = num
    print(smallest)


find_smallest(numbers)
