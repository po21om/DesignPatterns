"""Module implementing JokeAPI Connector"""
import json
from typing import Dict, Union

import requests

from singleton.singleton_metaclass import SingletonMeta


# pylint: disable=too-few-public-methods
class JokeAPIConnector(metaclass=SingletonMeta):
    """Connector for JokeAPI"""
    def __init__(self):
        self.base_url: str = "https://v2.jokeapi.dev"
        self.headers: Dict[str, str] = {"Accept": "application/json"}
        self._response: Union[requests.Request, None] = None

    def _build_path(self, *args: str) -> str:
        return f"{self.base_url}/{'/'.join(args)}?type=single"

    @staticmethod
    def _build_error_message(status_code: int, message: str) -> Dict[str, str]:
        return {"Error": f"{status_code}: {message}"}

    def get_joke(self, category: str = "Any") -> Union[Dict, str]:
        """
        Returns a random joke

        :param category:
        :return:
        """
        self._response = requests.request("GET",
                                          self._build_path("joke", category),
                                          headers=self.headers)
        if self._response.ok:
            return json.loads(self._response.text).get('joke')
        error = json.loads(self._response.text)
        return self._build_error_message(self._response.status_code,
                                         error.get('message'))


if __name__ == '__main__':
    joke = JokeAPIConnector()
    print(joke)
    print(joke.get_joke())
    joke2 = JokeAPIConnector()
    print(joke2)
    print(joke2.get_joke())
