# The metaclass definition, note the inheritance of type instead
# of object
class MetaSandwich(type):
    # Notice how the __new__ method has the same arguments
    # as the type function we used earlier?
    def __new__(metaclass, name, bases, namespace):
        name = 'SandwichCreatedByMeta'
        bases = (int,) + bases
        namespace['lettuce'] = 1
        return type.__new__(metaclass, name, bases, namespace)

"""    
class Sandwich(object):
    pass

Sandwich.__name__
'Sandwich'
issubclass(Sandwich, int)
False
Sandwich.lettuce
Traceback (most recent call last):
    ...
AttributeError: type object 'Sandwich' has no attribute 'lettuce'

"""
class Sandwich(object, metaclass=MetaSandwich):
    pass

Sandwich.__name__
'SandwichCreatedByMeta'
issubclass(Sandwich, int)
True
Sandwich.lettuce
1


class AddClassAttributeMeta(type):
    def __init__(metaclass, name, bases, namespace, **kwargs):
        # The kwargs should not be passed on to the
        # type.__init__
        type.__init__(metaclass, name, bases, namespace)
    def __new__(metaclass, name, bases, namespace, **kwargs):
        for k, v in kwargs.items():
            # setdefault so we don't overwrite attributes
            namespace.setdefault(k, v)
        return type.__new__(metaclass, name, bases, namespace)

class WithArgument(metaclass=AddClassAttributeMeta, a=1234):
    pass

WithArgument.a
1234
with_argument = WithArgument()
with_argument.a
1234
