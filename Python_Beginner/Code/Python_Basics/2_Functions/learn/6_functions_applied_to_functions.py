def mult_by_five(x):
    return 5 * x


# Passing function and argument
def call(fn, arg):
    """Call fn or arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn or arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n'
)
