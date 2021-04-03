from abc import abstractmethod
from abc import ABC
from Config import configure_session


class WebScrapper(ABC):
    products = list()
