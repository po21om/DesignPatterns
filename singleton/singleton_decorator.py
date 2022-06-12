"""Module implementing singleton with decorator"""


def singleton(class_):
    """kanapka"""
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    return get_instance


# pylint: disable=too-few-public-methods
@singleton
class FirstClass:
    """Just a FirstClass"""
    def __init__(self):
        self.val: int = 0


# pylint: disable=too-few-public-methods
@singleton
class SecondClass:
    """Just a SecondClass"""
    def __init__(self):
        self.val: int = 0


if __name__ == '__main__':
    a = FirstClass()
    print(a.val)
    a.val = 13
    b = FirstClass()
    print(b.val)
    print(a.val)

    c = SecondClass()
    print(c.val)
    c. val = 20
    d = SecondClass()
    print(c.val)
    print(d.val)
