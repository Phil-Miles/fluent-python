# Not only are Python functions real objects, but artibtraty Python objects may also
# be made to behave like functions. Implementing a __call__ instance method is all it
# takes.

print(f'Example 7-8. A BIngoCage does one thing: picks items from a shuffled list')
import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()
    # This creates a shortcut to bingo.pick() which is bingo()

bingo = BingoCage(range(3))
print(bingo())