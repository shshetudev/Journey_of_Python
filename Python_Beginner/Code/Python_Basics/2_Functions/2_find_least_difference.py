def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)
# Python isn't smart enough to read my code and turn it into a nice English description
# However, when i write a function, I can provide a description in what's called the docstring.
help(least_difference)
