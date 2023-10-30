print(f'Example 7-9. tag generates HTML elements; a keyword-only argument class_ is used '
      f'to pass "class" attributes as a workaround because class is a keyword in python')
def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'

print('1: A single positional argument produces an empty tag with that name.')
print('def tag(name, *content, class_=None, **attrs):')
print(tag('br'))
print('2: Any number of arguments after the first are captured by *content as a tuple')
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print('3: Keyword arguments not explicitly named in the tag signature are captured by '
      '**attrs as a dict.')
print(tag('p', 'hello', id=33))
print('4: The class_ parameter can only be passed as a keyword argument.')
print(tag('p', 'hello', 'world', class_='sidebar'))
print('5: The first positional argument can also be passed as a keyword.')
print(tag(content='testing', name='img'))
print('6: Prefixing the my_tag dict with ** passes all its items as separate arguments,'
      'which are then bound to the named parameters, with the remaining caught by '
      '**attrs.')
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class':'framed'}
print(tag(**my_tag))

