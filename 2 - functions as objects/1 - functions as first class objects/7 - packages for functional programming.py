# Example 7-11. Factorial implemented with reduce and an anonymous function
from functools import reduce

def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

# Example 7-12. Factorial implemented with reduce and operator .mul
from operator import mul

def factorial_(n):
    return reduce(mul, range(1, n+1))
# Reduce first takes the first two values of an iterable.
# For each following execution, the first argument is assigned the value of the previous function
# and the second argument is assigned the next value from the iterable.

# Example 7-13. Demo of itemgetter to sort a list of tuples
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

from operator import itemgetter
# itemgetter(1) creates a function that, given a collection, returns the
# item at index 1. That's easier to write and read than lambda fields: fields[1],
# which does the same thing.
for city in sorted(metro_data, key=itemgetter(1)):
    #print(city)
    pass

# If you pass multiple index arguments to itemgetter, the function it builds will return
# tuples with the extracted values, which is useful for sorting on multiple keys:
cc_name = itemgetter(1, 0)
for city in metro_data:
    #print(cc_name(city))
    pass
# Example 7-14. Demo of attrgetter to process a previously defined list of namedtuple
# called metro_data

from collections import namedtuple

LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
               for name, cc, pop, (lat, lon) in metro_data]
print(metro_areas[0])

from operator import attrgetter
# attrgetter is used to extract one or more attributes from an object
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    # attrbetter object name_lat is used here to extract the two targeted attributes
    # from each iterated object
    print(name_lat(city))

# printing the names of functions defined in operator
import operator
operators = [name for name in dir(operator) if not name.startswith('_')]
print(operators)