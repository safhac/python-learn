from functools import partial


class ClassMethod:
    def __init__(self, func):
        # func.__isabstractmethod__ = True
        self.func = func

    def __get__(self, instance, owner):
        print(f"{self=} {instance=} {owner=}")
        return partial(self.func, owner)


class Property:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(f"__get__ {self} {instance} {owner}")
        if not instance:
            return self

    def __call__(self, *args, **kwargs):
        print("call")