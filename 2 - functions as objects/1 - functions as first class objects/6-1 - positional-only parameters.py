# To ddefine a function requiring positional-only parameters, use / in the parameter list.
def div_mod(a, b, /):
    return (a // b, a % b)

# all arguments to the left of the / are positiona-only. After the /, you may specify
# other arguments, which work as usual

# Function from the previous example could be written as:
# def tag(name, /, *content, class_=None, **attrs):
