# Naive implementation
class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def __init__(self):
        if not self.__instance:
            print("First object of the class, shared instance doesn't exist yet!")
        self.val = 0

    def print_val(self):
        print(self.val)


if __name__ == '__main__':
    a = Singleton.get_instance()
    a.print_val()  # 0
    a.val = 10
    a.print_val()  # 10

    b = Singleton.get_instance()
    b.print_val()  # 10
    print(a)
    print(b)
