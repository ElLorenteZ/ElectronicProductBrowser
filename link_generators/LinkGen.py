"""
Robert Radzik
El-Ayachi Jr Stitou


"""
from abc import abstractmethod
from abc import ABC
import requests

from Config import configure_session


class LinkGen(ABC):

    def __init__(self, query_string_base, separator, page_string, shop_name, product_name):
        self.query_string_base = query_string_base
        self.separator = separator
        self.page_string = page_string
        self.shop_name = shop_name
        product_name = product_name.strip()
        product_name = product_name.replace(" ", self.separator)
        self.query_string = self.query_string_base + product_name
        self.product_url = ""
        self.max_pages = 0
        try:
            self.get_page_info()
        except requests.exceptions.Timeout:
            print("Error during request to: " + self.query_string)
            print("Connection timeout..")
        except requests.exceptions.TooManyRedirects:
            print("Error during request to: " + self.query_string)
            print("Too many redirects..")
        except requests.exceptions.RequestException as error:
            print("Error during request to: " + self.query_string)
            raise SystemError(error)

    def get_page_info(self):
        session = configure_session()
        response = session.get(self.query_string)
        self.product_url = response.url.replace(" ", "%20")
        self.max_pages = self.get_last_page_number(response.content)
        session.close()
        return

    def get_links_list(self):
        links_list = list()
        if self.max_pages == 1:
            links_list.append(self.product_url)
        elif self.max_pages > 1:
            for i in range(self.max_pages):
                link_page_i = self.product_url + self.page_string + str(i+1)
                links_list.append(link_page_i)
        return links_list

    @abstractmethod
    def get_last_page_number(self, content):
        pass




