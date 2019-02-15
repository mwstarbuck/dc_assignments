# this makes a pyramid
def make_a_pyramid():
    spaces = 8  # counts spaces to print
    stars = 1  # counts * to print
    while spaces >= 0:
        print(" " * spaces + "*" * stars)
        spaces -= 1
        stars += 2


make_a_pyramid()
