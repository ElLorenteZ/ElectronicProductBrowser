from link_generators.LinkGen import LinkGen
from bs4 import BeautifulSoup

SEPARATOR = "+"
QUERY_STRING_BASE = "https://www.oleole.pl/search.bhtml?keyword="
PAGE_STRING = "&page="
SHOP_NAME = "OleOle!"


class OleOleLinkGen(LinkGen):

    def __init__(self, product_name):
        super().__init__(QUERY_STRING_BASE, SEPARATOR, PAGE_STRING, SHOP_NAME, product_name)

    def get_last_page_number(self, content):
        bs = BeautifulSoup(content, 'html.parser')
        max_pages_divs = bs.find_all('a', class_="paging-number")
        if len(max_pages_divs) > 1:
            return int(max_pages_divs[-1].get_text())
        return 1
