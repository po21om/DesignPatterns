
# Make class Cake a Singleton
class Cake:
    def __init__(self):
        self._name: str = ""

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name


if __name__ == '__main__':
    cake_1 = Cake()
    cake_1.set_name("Makowiec")
    cake_2 = Cake()
    cake_2.set_name("Szarlortka")
    if cake_1.get_name() == cake_2.get_name():
        print("I'm a Singleton!")
    else:
        print("I'm not Singleton :(")
