# A function that takes a function as an argument or returns a function as the result is a
# higher-order function.

print(f'Example 7-3. Sorting a list of words by length\n')
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

print(f'\nExample 7-4. Sorting a list of words by their reversed spelling')


def reverse(word):
    return word[::-1]


print(reverse('testing'))
print(sorted(fruits, key=reverse))
