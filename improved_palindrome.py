word = input("Please enter a word: ")

l_word = word.lower()


# reverse the string


def reverse(entry):
    rev_word = ""
    for i in range(len(entry) - 1, -1, -1):
        rev_word += entry[i]
    return rev_word

# determin if it is a palindrome


def is_palindrome(entry, rev_entry, word):
    result = False
    if entry == rev_entry:
        #print(f"{word} is a palindrome!")
        result = True

    return result


result = is_palindrome(l_word, reverse(l_word), word)

if result:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is NOT a palindrome!")

# method found online better!

# def reverse_2(entry):
#    rev_word = ""
#    for i in entry:
#        rev_word = i + rev_wor
#    print(rev_word)


# reverse_2(word)

# FROM NOW ON USE:  reversed(string)
# Example: new_word = reversed(word)
