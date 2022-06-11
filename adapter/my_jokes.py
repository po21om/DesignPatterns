import random
from typing import Union, Dict

from singleton.jokeapi_connector import JokeAPIConnector


class MyJokes:
    def __init__(self):
        self._jokes = []

    def get_joke(self) -> str:
        return random.choice(self._jokes)


class JokeAPIAdapter(JokeAPIConnector, MyJokes):
    def __init__(self):
        super().__init__()

    def get_joke(self, category: str = "Any") -> Union[Dict, str]:
        return JokeAPIConnector.get_joke(self)


if __name__ == '__main__':
    joke = JokeAPIAdapter()
    print(joke)
    print(joke.get_joke())
