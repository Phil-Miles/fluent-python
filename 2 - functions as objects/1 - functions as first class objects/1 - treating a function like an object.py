print(f'\nExample 7-1. Create and test a function, then read its __doc__ and check its type\n')


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

print(f'\nExample 7-2. Use factorial through a different name, and pass factorial as an argument\n')
fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))

