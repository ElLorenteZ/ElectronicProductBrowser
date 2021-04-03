from abc import abstractmethod
from abc import ABC
from Config import configure_session
from bs4 import BeautifulSoup


class WebScrapper(ABC):
    products = list()

    def get_raw_elements(self, link, element, classes):
        session = configure_session()
        response = session.get(link)
        bs = BeautifulSoup(response.content, 'html.parser')
        print(bs.prettify())
        print(bs.find_all(element, class_=classes))
        return bs.find_all(element, class_=classes)
