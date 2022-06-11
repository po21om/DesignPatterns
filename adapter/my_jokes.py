import random

from singleton.jokeapi_connector import JokeAPIConnector


class MyJokes:
    def __init__(self):
        self._jokes = []

    def get_joke(self) -> str:
        return random.choice(self._jokes)


class JokeAPIAdapter(JokeAPIConnector):
    pass


if __name__ == '__main__':
    joke = JokeAPIAdapter()
    print(joke.get_joke())
