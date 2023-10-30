# Functional languages commonly offer the map, filter and reduce higher-order
# functions. The map and filter are still built-ins in Python 3, but since
# the introduction of list comprehensions and generator expressions, they
# are not as important.
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)


print(f'Example 7-5. List of factorials produced with map and filter compared to alternatives '
      f'coded as list comprehensions\n')
print(list(map(factorial, range(6))))
print([factorial(n) for n in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

print(f'\nExample 7-6. Sum of integers up to 99 performed with reduce and sum')
from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))

# Other reducing built-ins are all and any
# all(iterable) >> True if no elements are False
# any(iterable) >> True if any element is True
