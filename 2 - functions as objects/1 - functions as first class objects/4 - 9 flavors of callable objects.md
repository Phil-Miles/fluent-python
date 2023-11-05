call () operator can be used on:
1. User-defined functions - created with def statements or lambda expressions.
2. Built-in functions - a function implemented in C (for CPython), like len or time.strftime.
3. Built-in methods - methods implemented in C, like dict.get.
4. Methods - functions defined in the body of a class.
5. Classes - when invoked, a class runs its __new__ method to create an instance, then __init__ to initialize it,
and finally the instance is returned to the caller.
6. Class instances - if a class defines a __call__ method, the its instances may be invoked as functions
7. Generator functions - functions or methods that use the yield keyword in their body. When called, they return
a generator object
8. Native coroutine functions - Functions or methods defined with async def. When called, they return 
a coroutine object.
9. Asynchronous generator functions - Functions or methods defined with async def that have yield in their body.
When called, they return an asynchronous generator for use with async for.