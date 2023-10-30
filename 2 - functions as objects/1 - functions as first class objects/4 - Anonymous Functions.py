# The lambda keyword creates an anomymous function within a Python expression
print(f'Example 7-7. Sorting a list of words by their spelling using lambda\n')
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))

# If you find a piece of code hard to understand because of a lambda, replace it with a regular function
