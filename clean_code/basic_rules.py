"""Używamy samotłumaczących się nazw zmiennych i metod"""
# d = 10
elapsed_time_in_days = 10

# def test_test_test(a, b):
#     return a + b

def add(a, b):
    return a + b

"""Nazwy klas powinny być rzeczownikami lub składać się z fraz z rzeczownikami"""
# class Keyboarding:
#     pass

class Keyboard:
    pass

"""Minimalizujemy liczbę argumentów w metodach kiedy się da"""

# def path_builder(a, b, c, d, e, f, g, h):
#     return f"{a}/{b}/{c}..."


def path_builder(*args):
    return f"{'/'.join(args)}"


"""Metody powinny robić jedną rzecz i nie powinny być mega długie"""

# def multiply(a, b):
#      suma = a + b
#      diff = a - b
#      div = a / b
#      return a * b


def multiply(a, b):
    return a * b

from python_style_guide import multiply

a = multiply(2, 3)