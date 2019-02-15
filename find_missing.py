numbers = [9, 8, 7, 6, 5, 3, 4, 1, 0]

# will sort list and find missing number


def find_missing(numbers):
    numbers.sort()
    for i in range(0, len(numbers)):
        # looking for missing number
        if i != numbers[i]:
            # if number does not equal index print out missing number and break out of loop
            print(f"Number {i} is missing!")
            break


# sort_ascending(numbers1)
find_missing(numbers)
